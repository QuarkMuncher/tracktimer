from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import uuid

engine = create_engine("sqlite:///./lite.db", echo=True)

meta = MetaData()

timestamps = Table(
    "TimeStamps",
    meta,
    Column("id", String, primary_key=True),
    Column("begin", Integer),
    Column("end", Integer),
    Column("ProjectID", String),
)

projects = Table(
    "Projects",
    meta,
    Column("id", String, primary_key=True),
    Column("ProjectName", String),
)

meta.create_all(engine)


def get_id():
    return uuid.uuid1().hex


def find_projects():
    select_projects = projects.select()
    conn = engine.connect()
    result = conn.execute(select_projects).fetchall()
    return result


def project_exists(name):
    select_project = projects.select().where(projects.c.ProjectName == name)
    conn = engine.connect()
    result = conn.execute(select_project).fetchall()
    print(result)
    if len(result) >= 1:
        return True
    else:
        return False


def insert_project(name):
    if project_exists(name):
        print("Project already exists.")
    else:
        new_project = projects.insert().values(id=get_id(), ProjectName=name)
        conn = engine.connect()
        conn.execute(new_project)


#
# Below this comment there is currently being worked on a function
# for starting a timer
#

# def insert_start_timestamp(name):
#     if project_exists(name):
