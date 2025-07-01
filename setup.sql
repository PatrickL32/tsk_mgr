CREATE TABLE IF NOT EXISTS task(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR (64),
    sumary VARCHAR(128),
    descripton TEXT,
    is_done BOOLEAN DEFAULT 0
);

    --Insert some dummy data to test_with:
    INSERT INTO task(
        name,
        sumary,
        descripton) VALUES
    ("wash the car",
    "take the car to the car wash",
    "make sure  it gets vacuumed and waxed"
    ),
    ("walk the dog",
    "fido  neeeds a walk",
    "Three laps around the park"
    ),
    ("buy groceries",
    "Go to the supermarket",
    "We need : eggs milk and bread"
    );