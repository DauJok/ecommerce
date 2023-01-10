import pytest
from django.contrib.auth.models import User
from django.core.management import call_command


@pytest.fixture
def create_super_user(django_user_model):
    """Create and return django admin user"""
    return django_user_model.objects.create_superuser(
        "admin", "admin@admin.com", "safepassword"
    )


@pytest.fixture(scope="session")
def django_fixture_setup(django_db_blocker, django_db_setup):
    """Load DB data fixtures"""
    # Unblock database access since its not allowed by default.
    with django_db_blocker.unblock():
        # Loading fixtures with management command
        call_command("loaddata", "db_admin_fixture.json")
        call_command("loaddata", "db_category_fixture.json")
        call_command("loaddata", "db_product_fixture.json")
