import random

from django.core.management.base import BaseCommand

from plugins.shop_plugin.models import Product


class Command(BaseCommand):
    help = "Populate the shop with dummy products including images"

    def add_arguments(self, parser):
        parser.add_argument(
            "--count", type=int, default=10, help="Number of products to create"
        )

    def handle(self, *args, **options):
        count = options["count"]

        # Product categories and descriptions for more realistic data
        categories = ["Electronics", "Clothing", "Home & Kitchen", "Books", "Sports"]

        # Lists for generating product names
        adjectives = [
            "Premium",
            "Deluxe",
            "Essential",
            "Modern",
            "Classic",
            "Advanced",
            "Elegant",
            "Professional",
        ]
        nouns = [
            "Monitor",
            "Laptop",
            "Shirt",
            "Jeans",
            "Chair",
            "Table",
            "Cookware",
            "Novel",
            "Fitness Tracker",
        ]

        # Create dummy products
        for i in range(count):
            category = random.choice(categories)
            adjective = random.choice(adjectives)
            noun = random.choice(nouns)

            # Create a realistic product name
            name = f"{adjective} {category} {noun}"

            # Generate a realistic price
            price = round(random.uniform(9.99, 999.99), 2)

            # Generate a detailed description
            description = f"""
            Experience the quality of our {adjective.lower()} {category.lower()} {noun.lower()}.

            This product features high-quality materials and expert craftsmanship, designed to meet your everyday needs.
            Perfect for home, office, or on-the-go use.

            • Premium quality
            • Durable construction
            • Modern design
            • 1-year warranty
            """

            # Get a random image from placekitten.com, picsum.photos, or placecorgi.com
            image_services = [
                f"https://picsum.photos/id/{random.randint(1, 200)}/800/600",  # Lorem Picsum
                f"https://placekitten.com/{random.randint(800, 900)}/{random.randint(600, 700)}",  # PlaceKitten
                f"https://place.dog/{random.randint(800, 900)}/{random.randint(600, 700)}",  # Place Dog
            ]
            image_url = random.choice(image_services)

            # Create the product
            product = Product.objects.create(
                name=name,
                description=description,
                price=price,
                image_url=image_url,
                is_active=True,
            )

            self.stdout.write(self.style.SUCCESS(f"Created product: {product.name}"))

        self.stdout.write(self.style.SUCCESS(f"Successfully created {count} products"))
