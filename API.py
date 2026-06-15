# ============================================================
# LIMKOKWING UNIVERSITY LIBRARY MANAGEMENT API SIMULATION
# ============================================================
# COURSEWORK: ASYNCHRONOUS API IMPLEMENTATION USING PYTHON
#
# This program simulates a simple digital library system.
# Features Included:
# 1. View available books
# 2. Borrow books
# 3. Return books
# 4. Track overdue fines
# 5. Multiple users accessing the system simultaneously
# 6. Uses async and await for asynchronous programming
# 7. Includes Python type annotations
# ============================================================

import asyncio
from typing import Dict, List


# ============================================================
# SAMPLE LIBRARY DATABASE
# ============================================================

books: List[Dict[str, str | bool | int]] = [
    {
        "id": "BK101",
        "title": "Python Programming Fundamentals",
        "author": "John Smith",
        "category": "Programming",
        "available": True,
        "fine_per_day": 2
    },
    {
        "id": "BK102",
        "title": "Introduction to Database Systems",
        "author": "Alice Johnson",
        "category": "Database",
        "available": True,
        "fine_per_day": 3
    },
    {
        "id": "BK103",
        "title": "Modern Web Development",
        "author": "Michael Brown",
        "category": "Technology",
        "available": True,
        "fine_per_day": 4
    }
]


# ============================================================
# ENDPOINT 1: GET /books
# Purpose:
# Display all books currently stored in the library system
# ============================================================

async def get_books() -> List[Dict[str, str | bool | int]]:
    print("\nLoading books from library database...\n")

    # Simulate database/server delay
    await asyncio.sleep(1)

    return books


# ============================================================
# ENDPOINT 2: POST /borrow
# Purpose:
# Allow a user to borrow a book
# ============================================================

async def borrow_book(user: str, book_id: str) -> str:

    print(f"{user} is trying to borrow book {book_id}...")

    # Simulate processing delay
    await asyncio.sleep(2)

    for book in books:

        if book["id"] == book_id:

            if book["available"]:
                book["available"] = False

                return (
                    f"SUCCESS: {user} borrowed "
                    f"'{book['title']}' successfully."
                )

            else:
                return (
                    f"FAILED: Sorry {user}, "
                    f"'{book['title']}' is already borrowed."
                )

    return f"ERROR: Book ID {book_id} not found in the library."


# ============================================================
# ENDPOINT 3: POST /return
# Purpose:
# Allow users to return borrowed books
# ============================================================

async def return_book(user: str, book_id: str) -> str:

    print(f"{user} is returning book {book_id}...")

    await asyncio.sleep(2)

    for book in books:

        if book["id"] == book_id:

            if not book["available"]:
                book["available"] = True

                return (
                    f"SUCCESS: {user} returned "
                    f"'{book['title']}' successfully."
                )

            else:
                return (
                    f"NOTICE: '{book['title']}' "
                    f"was not borrowed."
                )

    return f"ERROR: Book ID {book_id} does not exist."


# ============================================================
# ENDPOINT 4: GET /fine
# Purpose:
# Calculate overdue fine for a borrowed book
# ============================================================

async def calculate_fine(book_id: str, overdue_days: int) -> str:

    await asyncio.sleep(1)

    for book in books:

        if book["id"] == book_id:

            fine: int = overdue_days * int(book["fine_per_day"])

            return (
                f"Book: {book['title']} | "
                f"Overdue Days: {overdue_days} | "
                f"Total Fine: Le {fine}"
            )

    return "Book not found for fine calculation."


# ============================================================
# MAIN PROGRAM
# Simulates multiple users accessing the library system
# at the same time using asyncio.gather()
# ============================================================

async def main() -> None:

    print("\n================================================")
    print(" LIMKOKWING LIBRARY DIGITAL API SYSTEM STARTED ")
    print("================================================")

    # --------------------------------------------------------
    # Display available books
    # --------------------------------------------------------

    available_books = await get_books()

    print("AVAILABLE BOOKS IN THE LIBRARY:\n")

    for book in available_books:
        print(book)

    # --------------------------------------------------------
    # Multiple users borrowing books simultaneously
    # --------------------------------------------------------

    print("\n================================================")
    print(" MULTIPLE USERS BORROWING BOOKS SIMULTANEOUSLY ")
    print("================================================\n")

    borrow_results = await asyncio.gather(
        borrow_book("Bintu", "BK101"),
        borrow_book("David", "BK102"),
        borrow_book("Isha", "BK101")
    )

    for result in borrow_results:
        print(result)

    # --------------------------------------------------------
    # Returning books simultaneously
    # --------------------------------------------------------

    print("\n================================================")
    print(" MULTIPLE USERS RETURNING BOOKS ")
    print("================================================\n")

    return_results = await asyncio.gather(
        return_book("Bintu", "BK101"),
        return_book("David", "BK102")
    )

    for result in return_results:
        print(result)

    # --------------------------------------------------------
    # Fine Calculation
    # --------------------------------------------------------

    print("\n================================================")
    print(" OVERDUE FINE CALCULATION ")
    print("================================================\n")

    fine_result = await calculate_fine("BK103", 5)

    print(fine_result)

    print("\n================================================")
    print(" LIBRARY API SIMULATION COMPLETED SUCCESSFULLY ")
    print("================================================")


# ============================================================
# PROGRAM EXECUTION
# ============================================================

asyncio.run(main())