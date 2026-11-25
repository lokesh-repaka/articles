package bank.ai.governance

import future.keywords.in

default allow = false
default require_human_approval = false

# Allow read-only invoice queries for authorized roles
allow {
    input.action == "VIEW_INVOICES"
    "invoice_viewer" in input.user.client_roles
}

# Allow invoice processing within automated threshold
allow {
    input.action == "PROCESS_INVOICE"
    "invoice_processor" in input.user.client_roles
    input.amount <= 10000
}

# Require human approval for transactions above limit
require_human_approval {
    input.action == "PROCESS_INVOICE"
    "invoice_processor" in input.user.client_roles
    input.amount > 10000
}

# Block all destructive database operations
deny {
    input.sql_statement_type in ["DROP", "DELETE", "TRUNCATE", "ALTER"]
}

is_authorized {
    allow
    not deny
    not require_human_approval
}
