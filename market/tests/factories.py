import factory
import pytest
from faker import Faker
from pytest_factoryboy import register

fake = Faker()

from market.inventory import models


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    name = fake.lexify(text="cat_name_??????")
    slug = fake.lexify(text="cat_slug_??????")


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Product

    web_id = factory.Sequence(lambda n: "web_id_%d" % n)
    name = fake.lexify(text="prod_name_??????")
    slug = fake.lexify(text="prod_slug_??????")
    description = fake.text()
    is_active = True
    created_at = "2023-01-09 20:18:33.279092"
    updated_at = "2023-01-09 20:18:33.279092"

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create or not extracted:
            return

        # Add categories associated with product
        if extracted:
            for cat in extracted:
                self.category.add(cat)


register(CategoryFactory)
register(ProductFactory)
