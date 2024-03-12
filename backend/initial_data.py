from app import app
from backend.models import db, User, Role, Album, Song, Playlist
with app.app_context():
  db.create_all()
  # Check if Role table is empty
  if not db.session.query(Role.query).first():
    roles_data = [{
        "id":
        "adm",
        "name":
        "Admin",
        "description":
        "Administrator - has rights to remove a song or an album, access to user usage statistics. There is only one admin in the system"
    }, {
        "id":
        "art",
        "name":
        "Artist",
        "description":
        "Artist - has rights to add and manage songs and albums and has previliges of regular user too"
    }, {
        "id":
        "usr",
        "name":
        "User",
        "description":
        "User - regular user with access to playlists and songs"
    }]
    for role_info in roles_data:
      role = Role(id=role_info["id"],
                  name=role_info["name"],
                  description=role_info["description"])
      db.session.add(role)
    db.session.commit()
    print("Roles added successfully")

  # Check if admin is present
  is_admin_present = db.session.query(
      User.role_id == "admin").first() is not None
  if not is_admin_present:
    admin = User(id=0,
                 name="Admin01",
                 username="admin01",
                 email="admin01@vibezz.com",
                 password="admin",
                 role_id="adm")
    db.session.add(admin)
    db.session.commit()
    print("Admin created")
