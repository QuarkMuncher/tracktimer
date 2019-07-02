from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import uuid
from time import time
from datetime import timedelta

engine = create_engine("sqlite:///./lite.db")

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
    if len(result) >= 1:
        return True
    else:
        return False


def insert_project(name):
    if project_exists(name):
        return f"Project: {name} already exists."
    else:
        new_project = projects.insert().values(id=get_id(), ProjectName=name)
        conn = engine.connect()
        conn.execute(new_project)
        return f"Project: {name} created"


def timer_running():
    timer = timestamps.select().where(timestamps.c.end.is_(None))
    conn = engine.connect()
    result = conn.execute(timer).fetchall()
    if len(result) > 0:
        return True
    else:
        return False


def start_timer(name):
    try:
        if not timer_running():
            if project_exists(name):
                select_project = projects.select().where(
                    projects.c.ProjectName == name
                )
                conn = engine.connect()
                ident, _ = conn.execute(select_project).fetchone()
                if ident:
                    insert_timestart = timestamps.insert().values(
                        id=get_id(), begin=time(), ProjectID=ident
                    )
                    insert_timestart.compile(engine)
                    conn = engine.connect()
                    conn.execute(insert_timestart)
                    return f"Timer for '{name}' started.'"
                else:
                    return "Unknown error"
            else:
                return "No such project"
        else:
            return "A timer is already running"
    except Exception as e:
        return f"Unknow error: {e}"


def stop_timer():
    try:
        if timer_running():
            current_time = time()
            conn = engine.connect()
            timer_started_at = timestamps.select().where(
                timestamps.c.end.is_(None)
            )
            _, begin, _, _ = conn.execute(timer_started_at).fetchone()
            timer_stop = (
                timestamps.update()
                .where(timestamps.c.end.is_(None))
                .values(end=current_time)
            )
            conn.execute(timer_stop)
            time_passed = str(timedelta(seconds=round(current_time - begin)))
            return f"Timer stopped, {time_passed} has passed."
    except Exception:
        return "ERROR"


def report_range(begin, end):
    try:

        conn = engine.connect()
        # Write querying of what to get.
        select = (
            timestamps.select()
            .where(timestamps.c.begin < begin)
            .where(timestamps.c.end > end)
        )
        result = conn.execute(select)

    except Exception as identifier:
        return f"Go fuck yourself {identifier}"
