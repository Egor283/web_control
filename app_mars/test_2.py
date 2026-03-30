from requests import get

print(get("https://127.0.0.1:5000/api/jobs").json())
print(get("https://127.0.0.1:5000/api/jobs",
          json={"job": "install comp"}).json())
print(get("https://127.0.0.1:5000/api/jobs",
          json={"job": "install comp", "team_leader": 2, "work_size": 3,
                "collaborators": "1, 3", "is_finished": False}).json())
print(get("https://127.0.0.1:5000/api/jobs").json())