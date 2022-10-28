from models.Project import Project
from models.Category import Category
from scripts import card_script, category_script
from models.Card import Card

def addNew(db, payload):
    project = Project(user_id=payload.user_id, title=payload.title)
    db.add(project)
    db.commit()
    db.refresh(project)

    categories = [
        Category(project_id=project.id, title="Backlog", color="#2563eb"),
        Category(project_id=project.id, title="To-Do", color="#ea580c"),
        Category(project_id=project.id, title="Doing", color="#ea580c"),
        Category(project_id=project.id, title="Code Review", color="#ea580c"),
        Category(project_id=project.id, title="Testing", color="#ea580c"),
        Category(project_id=project.id, title="Done", color="#16a34a"),
    ]

    db.bulk_save_objects(categories)
    db.commit()

    return project


def getAllProjects(db, userID):
    print(db.query(Project).filter(Project.user_id == userID).all())
    return db.query(Project).filter(Project.user_id == userID).all()


def removeProject(db, Project_id):
    category_script.getCategoryByProject(db, Project_id).delete()
    

    db.query(Project).filter(Project.id == Project_id).delete()
    db.commit()
    return True
