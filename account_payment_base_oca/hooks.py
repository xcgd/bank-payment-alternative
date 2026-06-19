import logging

from odoo.tools.sql import column_exists, create_column

_logger = logging.getLogger(__name__)


def pre_init(env):
    _logger.info("DATA MIG: Add fixed value for bank_account_link")
    if not column_exists(env.cr, "account_payment_method_line ", "bank_account_link"):
        create_column(env.cr, "account_payment_method_line ", "bank_account_link", "varchar")
    env.cr.execute(
        "UPDATE account_payment_method_line SET bank_account_link='fixed' WHERE bank_account_link is null"
    )
