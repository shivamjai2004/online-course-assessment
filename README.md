# Django Online Course – Assessment Project

This starter project implements the Question, Choice and Submission models, Django admin configuration, Bootstrap course detail page, exam submission and result evaluation.

## 1. Setup (Windows PowerShell)

```powershell
cd online-course-assessment
py -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py makemigrations onlinecourse
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/admin/ and sign in with the superuser.

## 2. Add sample content in admin

1. Create an Instructor and a Learner (the learner must be linked to a Django user).
2. Create a Course.
3. Create a Lesson under the course.
4. In the Lesson edit page, add questions using the Questions inline.
5. Open each Question and add choices; mark exactly one choice as correct.
6. Visit `/course/1/` (replace 1 with your course ID).
7. Log in as the learner at `/admin/login/` only if the learner account has staff access; for normal learner testing, use Django's login flow or temporarily make the learner user staff for local testing. Do not use the admin account as the learner if you want the learner profile to be distinct.

## 3. Required assignment files

- `onlinecourse/models.py`
- `onlinecourse/admin.py`
- `onlinecourse/templates/onlinecourse/course_details_bootstrap.html`
- `onlinecourse/views.py`
- `onlinecourse/urls.py`

## 4. GitHub

Create a public GitHub repository, then from this folder run:

```bash
git init
git add .
git commit -m "Complete Django online course assessment"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/online-course-assessment.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. Do not commit `db.sqlite3`, passwords, or secret keys used in production.

## Important notes

- This is a clean starter implementation based on the assignment description, not a copy of your course lab's hidden starter repository. If your lab supplied pre-existing Course/Lesson models or exact field names, merge these features into that project rather than replacing it blindly.
- The exam submission view requires an authenticated Django user and creates/uses a Learner profile for that user.
- For the screenshot named `07-final.png`, submit the exam with enough correct answers to reach at least 70% so the page displays “Congratulations!”.
- The admin screenshot must show both “Authentication and Authorization” and “OnlineCourse” sections on the same admin index page.
