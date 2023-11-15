from opentelemetry.semconv.trace import SpanAttributes

METIS_DO_NOT_TRACK_COMMENT = "/*METIS_DO_NOT_TRACK*/"

METIS_REQUEST_SPAN_ATTRIBUTE_IDENTIFIER = "track.by.metis"
METIS_STATEMENT_SPAN_ATTRIBUTE = f"{SpanAttributes.DB_STATEMENT}.metis"
METIS_PLAN_SPAN_ATTRIBUTE = f"{METIS_STATEMENT_SPAN_ATTRIBUTE}.plan"

METIS_QUERY_SPAN_NAME = "metis-query"
EXPLAIN_SUPPORTED_STATEMENTS = (
    "SELECT",
    "INSERT",
    "UPDATE",
    "DELETE",
)
SENTRY_DSN = None  # This value is injected during the publishing process
SENTRY_DSN = "https://f4732683eb3a40ab9e5a5d4033b246e0@o1173646.ingest.sentry.io/6271090"
