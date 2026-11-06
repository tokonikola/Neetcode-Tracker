import sqlite3

def get_connection():
    con = sqlite3.connect("tracker.db")
    cur = con.cursor()
    
    #turn foreign keys on
    cur.execute("PRAGMA foreign_keys = ON")

    #create problems, categories, attempts tables
    cur.executescript("""
    CREATE TABLE IF NOT EXISTS categories(
        id INTEGER PRIMARY KEY,
        category TEXT UNIQUE NOT NULL
    );


    CREATE TABLE IF NOT EXISTS problems(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        difficulty TEXT NOT NULL,
        category_id INTEGER REFERENCES categories(id) NOT NULL,
        nurl TEXT,
        url TEXT NOT NULL,

        --SM-2 Values
        easiness REAL DEFAULT 2.5 NOT NULL,
        interval_days INTEGER DEFAULT 0 NOT NULL,
        repetitions INTEGER DEFAULT 0 NOT NULL,
        next_review_date TEXT DEFAULT NULL
    );

    CREATE TABLE IF NOT EXISTS attempts(
        id INTEGER PRIMARY KEY,
        problem_id INTEGER REFERENCES problems(id) NOT NULL,
        attempt_date TEXT NOT NULL,
        quality INTEGER NOT NULL,
        time_minutes INTEGER,
        insight TEXT,
        solution TEXT
    );
    """
    )
    return con