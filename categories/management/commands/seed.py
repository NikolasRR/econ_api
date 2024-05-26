from django.core.management.base import BaseCommand
from enum import Enum
from categories.models import Category
import logging

logger = logging.getLogger(__name__)

DESCRIPTIONS = [
    "Food",
    "Transport",
    "Health",
    "Education",
    "Entertainment",
    "Salary",
    "Investment",
    "Savings",
    "Gifts",
    "Donations",
    "Rent",
    "Utilities",
    "Clothing",
    "Electronics",
    "Home",
]


class Mode(Enum):
    REFRESH = "refresh"
    CLEAR = "clear"
    UPDATE = "update"


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument("--mode", type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write("seeding data...")
        run_seed(self, options["mode"])
        self.stdout.write("done.")


def clear_data():
    """Deletes all the table data"""
    logger.info("Delete Address instances")
    Category.objects.all().delete()


def create_category(description: str):
		category = Category(description=description)
		category.save()
		logger.info("{} address created.".format(category.description))


def run_seed(self, mode):
    match mode:
        case Mode.CLEAR:
            clear_data()
        case Mode.REFRESH:
            clear_data()
            for description in DESCRIPTIONS:
                create_category(description)
        case Mode.UPDATE:
            for description in DESCRIPTIONS:
                category = Category.objects.get(description=description)
                if category is None:
                    create_category(description)
                else:
                    category.description = description
        case _:
            raise Exception("Invalid mode")
