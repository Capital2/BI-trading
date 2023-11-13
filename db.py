from DWH import Base, engine

def init_db():
    Base.metadata.create_all(engine)
    
if __name__ == "__main__":
    try:
        init_db()
        print("Database initialized successfully")
    except Exception as e:
        print("Database initialization failed")
        print(e)