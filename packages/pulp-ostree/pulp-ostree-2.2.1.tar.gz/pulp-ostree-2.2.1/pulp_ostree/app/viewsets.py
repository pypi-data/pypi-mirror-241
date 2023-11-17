from gettext import gettext as _

from django_filters.filters import CharFilter
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from rest_framework.serializers import ValidationError

from pulpcore.plugin.viewsets import ReadOnlyContentViewSet, ContentFilter, NAME_FILTER_OPTIONS
from pulpcore.plugin import viewsets as core
from pulpcore.plugin.models import RepositoryVersion
from pulpcore.plugin.actions import ModifyRepositoryActionMixin
from pulpcore.plugin.serializers import (
    AsyncOperationResponseSerializer,
    RepositoryAddRemoveContentSerializer,
    RepositorySyncURLSerializer,
)
from pulpcore.plugin.tasking import dispatch

from . import models, serializers, tasks


class OstreeRemoteViewSet(core.RemoteViewSet):
    """A ViewSet class for OSTree remote repositories."""

    endpoint_name = "ostree"
    queryset = models.OstreeRemote.objects.all()
    serializer_class = serializers.OstreeRemoteSerializer


class OstreeRepositoryViewSet(core.RepositoryViewSet, ModifyRepositoryActionMixin):
    """A ViewSet class for OSTree repositories."""

    endpoint_name = "ostree"
    queryset = models.OstreeRepository.objects.all()
    serializer_class = serializers.OstreeRepositorySerializer

    @extend_schema(
        description="Trigger an asynchronous task to sync content.",
        summary="Sync from remote",
        responses={202: AsyncOperationResponseSerializer},
    )
    @action(detail=True, methods=["post"], serializer_class=RepositorySyncURLSerializer)
    def sync(self, request, pk):
        """Dispatch a sync task."""
        repository = self.get_object()
        serializer = RepositorySyncURLSerializer(
            data=request.data, context={"request": request, "repository_pk": pk}
        )
        serializer.is_valid(raise_exception=True)
        remote = serializer.validated_data.get("remote", repository.remote)
        mirror = serializer.validated_data.get("mirror")

        result = dispatch(
            tasks.synchronize,
            shared_resources=[remote],
            exclusive_resources=[repository],
            kwargs={
                "remote_pk": str(remote.pk),
                "repository_pk": str(repository.pk),
                "mirror": mirror,
            },
        )
        return core.OperationPostponedResponse(result, request)

    @extend_schema(
        description="Trigger an asynchronous task to import all refs and commits to a repository.",
        summary="Import refs and commits to a repository",
        responses={202: AsyncOperationResponseSerializer},
    )
    @action(detail=True, methods=["post"], serializer_class=serializers.OstreeImportAllSerializer)
    def import_all(self, request, pk):
        """Import all refs and commits to a repository."""
        repository = self.get_object()

        serializer = serializers.OstreeImportAllSerializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)

        artifact = serializer.validated_data["artifact"]
        repository_name = serializer.validated_data["repository_name"]

        async_result = dispatch(
            tasks.import_all_refs_and_commits,
            exclusive_resources=[artifact, repository],
            kwargs={
                "artifact_pk": str(artifact.pk),
                "repository_pk": str(repository.pk),
                "repository_name": repository_name,
            },
        )
        return core.OperationPostponedResponse(async_result, request)

    @extend_schema(
        description="Trigger an asynchronous task to append child commits to a repository.",
        summary="Append child commits to a repository",
        responses={202: AsyncOperationResponseSerializer},
    )
    @action(
        detail=True,
        methods=["post"],
        serializer_class=serializers.OstreeImportCommitsToRefSerializer,
    )
    def import_commits(self, request, pk):
        """Append child commits to a repository."""
        repository = self.get_object()

        serializer = serializers.OstreeImportCommitsToRefSerializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)

        artifact = serializer.validated_data["artifact"]
        repository_name = serializer.validated_data["repository_name"]
        ref = serializer.validated_data["ref"]

        async_result = dispatch(
            tasks.import_child_commits,
            exclusive_resources=[artifact, repository],
            kwargs={
                "artifact_pk": str(artifact.pk),
                "repository_pk": str(repository.pk),
                "repository_name": repository_name,
                "ref": ref,
            },
        )
        return core.OperationPostponedResponse(async_result, request)

    @extend_schema(
        description="Trigger an asynchronous task to modify content.",
        summary="Modify repository",
        responses={202: AsyncOperationResponseSerializer},
    )
    @action(
        detail=True,
        methods=["post"],
        serializer_class=RepositoryAddRemoveContentSerializer,
    )
    def modify(self, request, pk):
        """Queues a task that adds and remove content units within a repository."""
        repository = self.get_object()
        serializer = self.get_serializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)

        if "base_version" in request.data:
            base_version_pk = self.get_resource(request.data["base_version"], RepositoryVersion).pk
        else:
            base_version_pk = None

        task = dispatch(
            tasks.modify_content,
            exclusive_resources=[repository],
            kwargs={
                "repository_pk": pk,
                "base_version_pk": base_version_pk,
                "add_content_units": serializer.validated_data.get("add_content_units", []),
                "remove_content_units": serializer.validated_data.get("remove_content_units", []),
            },
        )
        return core.OperationPostponedResponse(task, request)

    def verify_content_units(self, content_units, all_content_units):
        """Verify referenced content units."""
        existing_content_units_pks = content_units.values_list("pk", flat=True)
        existing_content_units_pks = {str(pk) for pk in existing_content_units_pks}

        missing_pks = set(all_content_units.keys()) - existing_content_units_pks
        if missing_pks:
            missing_hrefs = [all_content_units[pk] for pk in missing_pks]
            raise ValidationError(
                _("Could not find the following content units: {}").format(missing_hrefs)
            )


class OstreeRepositoryVersionViewSet(core.RepositoryVersionViewSet):
    """A ViewSet class that represents a single OSTree repository version."""

    parent_viewset = OstreeRepositoryViewSet


class OstreeDistributionViewSet(core.DistributionViewSet):
    """A ViewSet class for OSTree distributions."""

    endpoint_name = "ostree"
    queryset = models.OstreeDistribution.objects.all()
    serializer_class = serializers.OstreeDistributionSerializer


class OstreeRefFilter(ContentFilter):
    """A filterset class for refs."""

    checksum = CharFilter(field_name="commit__checksum")

    class Meta:
        model = models.OstreeRef
        fields = {"name": NAME_FILTER_OPTIONS}


class OstreeRefViewSet(ReadOnlyContentViewSet):
    """A ViewSet class for OSTree head commits."""

    endpoint_name = "refs"
    queryset = models.OstreeRef.objects.all()
    serializer_class = serializers.OstreeRefSerializer
    filterset_class = OstreeRefFilter


class OstreeCommitFilter(ContentFilter):
    """A filterset class for commits."""

    class Meta:
        model = models.OstreeCommit
        fields = {"checksum": ["exact"]}


class OstreeCommitViewSet(ReadOnlyContentViewSet):
    """A ViewSet class for OSTree commits."""

    endpoint_name = "commits"
    queryset = models.OstreeCommit.objects.all()
    serializer_class = serializers.OstreeCommitSerializer
    filterset_class = OstreeCommitFilter


class OstreeObjectFilter(ContentFilter):
    """A filterset class for objects."""

    class Meta:
        model = models.OstreeObject
        fields = {"checksum": ["exact"]}


class OstreeObjectViewSet(ReadOnlyContentViewSet):
    """A ViewSet class for OSTree objects (e.g., dirtree, dirmeta, file)."""

    endpoint_name = "objects"
    queryset = models.OstreeObject.objects.all()
    serializer_class = serializers.OstreeObjectSerializer
    filterset_class = OstreeObjectFilter


class OstreeContentViewSet(ReadOnlyContentViewSet):
    """A ViewSet class for uncategorized content units (e.g., static deltas)."""

    endpoint_name = "content"
    queryset = models.OstreeContent.objects.all()
    serializer_class = serializers.OstreeContentSerializer


class OstreeConfigViewSet(ReadOnlyContentViewSet):
    """A ViewSet class for OSTree repository configurations."""

    endpoint_name = "configs"
    queryset = models.OstreeConfig.objects.all()
    serializer_class = serializers.OstreeConfigSerializer


class OstreeSummaryViewSet(ReadOnlyContentViewSet):
    """A ViewSet class for OSTree repository summary files."""

    endpoint_name = "summaries"
    queryset = models.OstreeSummary.objects.all()
    serializer_class = serializers.OstreeSummarySerializer
