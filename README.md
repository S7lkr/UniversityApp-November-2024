# < Documentation > #

## 1. Project description:
#### This project aims to simulate a real university structure, principles and functionalities. It has courses with lessons and comments. Gallery with albums, containing university photos. Library with books & magazines. Users (students & lectors) can join, quit or manage (CRUD) a course, depending on their granted user permission.

## ----------------------------------------------------------------------------------------------------

## 2. Project requirements:
#### - Python version: 3.9 or higher
#### - db.sqlite3 (integrated in django, by default will be created after running initial migrations)
#### - Browser: Project has been developed and tested on Brave v1.73.97 Chromium 131.0.6778.108(official build, 64-bit)
#### - Working resolution: 1920x1080 fullHD (not mandatory, but recommended)

## ----------------------------------------------------------------------------------------------------

## 3. Setup instructions:
#### 3.1 Start a new (base) Django project on your PC (django system files, cores and functionalities in order to run a project)
#### 3.2 Clone project (get it on your PC):
```angular2html
git clone https://github.com/S7lkr/UniversityApp-November-2024
```
#### 3.3 Make sure 'venv' (virtual environment) is properly configured and installed. If not (in python console):
```angular2html
python -m venv venv
```
#### 3.4 Install all dependencies (required python packages):
```angular2html
pip install -r requirements.txt
```

## ----------------------------------------------------------------------------------------------------

## (!!) 4. Configuration (VERY IMPORTANT!)
#### DISCLAIMER: In order for the project to work properly, make sure you CREATE THE GROUPS !!, given below & add the PERMISSIONS into them !!, correspondingly. This step is mandatory!

### 4.1 Authentication --> UniversityApp integrates and uses 4 MAIN TYPES of users:
#### - UnAuthenticated (no such user registered and existing in DB):
- [x] Guest (AnonymousUser) -> NO PERMISSIONS! Has the most limited access to the site. Can only VIEW: courses, comments, books, magazines, gallery.
#### - Authenticated (process: first IDENTIFICATION occurs -> system checks if they do exist as registered/saved/ users in DB, and only after that they are AUTHENTICATED and logged in system):
- [x] Student 
- [x] Lector
- [x] Moderator (staff) -> inherits all Lector permissions + full edit permissions on everything (except user Profiles), as well as limited delete permissions -> (del only) Comments, Albums, Photos, Courses, Lessons. 
- [x] Admin (superuser) -> The website's "GOD". HAS ALL PERMISSIONS available!

### 4.2 Authorization (Groups & Permissions): Django uses 'Groups' to grant & define a user's permissions. When checking if a user has a permission for CRUD, best practice is not to check WHICH GROUP he is in, but WHAT PERMISSIONS he has. This is how Authorization works in Django.
#### - STUDENT Group. Permissions: can only view and with extremely limited edit/del permissions: courses (join/quit them), profiles, lessons, comments (add/del their own only), books, magazines, gallery (albums & photos).
#### - LECTOR Group. Permissions: inherits all Student permissions + when joining a course, becomes its lector and ONLY THEN he can only EDIT course contents and data. Can also add books/magazines.
#### - MODERATOR Group. Permissions: inherits all Lector permissions + full CRUD for:
- [x] Courses
- [x] Lessons
- [x] Comments
- [x] Gallery (Albums & Photos)
- [x] Library (Books & Magazines)

### NOTE:
#### ONLY AFTER you have run the project & have users & profiles created, open admin panel on this url: http://localhost:8000/admin/ (make sure url ends up with 'slash', or Error occurs), Create these groups & Add corresponding permission into them:
| Group     | Permissions                               |
|-----------|-------------------------------------------|
| Student   | accounts-profile-Can view profile         |
|           | comments-comment-Can view comment         |
|           | courses-course-Can view course            |
|           | gallery-album-Can view album              |
|           | gallery-photo-Can view photo              |
|           | lessons-lesson-Can view lesson            |
|           | library-book-Can view book                |
|           | library-magazine-Can view magazine        |

| Group     | Permissions                               |
|-----------|-------------------------------------------|
| Lector    | accounts-profile-Can view profile         |
|           | comments-comment-Can add comment          |
|           | comments-comment-Can view comment         |
|           | courses-course-Can add course             |
|           | courses-course-Can change course          |
|           | courses-course-Can view course            |
|           | gallery-album-Can view album              |
|           | gallery-photo-Can view photo              |
|           | lessons-lesson-Can add lesson             |
|           | lessons-lesson-Can change lesson          |
|           | lessons-lesson-Can view lesson            |
|           | library-book-Can add book                 |
|           | library-book-Can view book                |
|           | library-magazine-Can add magazine         |
|           | library-magazine-Can view magazine        |

| Group     | Permissions                               |
|-----------|-------------------------------------------|
| Moderator | accounts-customuser-Can View custom user  |
|           | accounts-profile-Can view profile         |
|           | admin-logentry-Can view log entry         |
|           | auth-group-Can view group                 |
|           | comments-comment-full CRUD                |
|           | courses-course-full CRUD                  |
|           | gallery-album-full CRUD                   |
|           | gallery-photo-full CRUD                   |
|           | lessons-lesson-full CRUD                  |
|           | library-book-full CRUD                    |
|           | library-magazine-full CRUD                |
|           | sessions-session-Can view session         |


### 4.3 Flow data in DB, used default sqlite3 for this project (optional step, but recommended):

#### accounts_customuser:
| id | email                   | password  | is_active | is_staff | is_superuser |
|----|-------------------------|-----------|-----------|----------|--------------|
| 1  | admin@admin.com         | admin     | 1         | 1        | 1            |
| 2  | dido@dido.com           | 12admin34 | 1         | 0        | 0            |
| 3  | bob@bob.com             | 12admin34 | 1         | 0        | 0            |
| 4  | jasmine@jasmine.com     | 12admin34 | 1         | 0        | 0            |
| 5  | angie@angie.com         | 12admin34 | 1         | 0        | 0            |
| 6  | john@john.com           | 12admin34 | 1         | 0        | 0            |
| 7  | jack@jack.com           | 12admin34 | 1         | 0        | 0            |
| 8  | arthur@arthur.com       | 12admin34 | 1         | 0        | 0            |
| 9  | kate@kate.com           | 12admin34 | 1         | 0        | 0            |
| 10 | will@will.com           | 12admin34 | 1         | 0        | 0            |
| 11 | moderator@moderator.com | admin     | 1         | 1        | 0            |

#### accounts_profile:
| id | first_name | last_name   | personal_image                                  | age  | user_id | course_id | bio          | is_lector |
|----|------------|-------------|-------------------------------------------------|------|---------|-----------|--------------|-----------|
| 1  | Admin      | Admin       | http://127.0.0.1:8000/static/img/person1.jpg    | null | 1       | null      | null         | 0         |
| 2  | Diyan      | Kalaydzhiev | http://127.0.0.1:8000/static/img/team-1.jpg     | 20   | 2       | 4         | Nice person. | 1         |
| 3  | Bob        | Harrison    | http://127.0.0.1:8000/static/img/team-3.jpg     | 27   | 3       | 1         | Nice person. | 1         |
| 4  | Jasmine    | Lucas       | http://127.0.0.1:8000/static/img/team-2.jpg     | 31   | 4       | 3         | Nice person. | 1         |
| 5  | Angelina   | Jolie       | http://127.0.0.1:8000/static/img/team-4.jpg     | 39   | 5       | 2         | Nice person. | 1         |
| 6  | John       | Doe         | http://127.0.0.1:8000/static/img/student-jd.jpg | 52   | 6       | 1         | Nice person. | 0         |
| 7  | Jack       | Sparrow     | http://127.0.0.1:8000/static/img/student-js.jpg | 47   | 7       | 1         | Nice person. | 0         |
| 8  | Arthur     | Morgan      | http://127.0.0.1:8000/static/img/student-am.jpg | 38   | 8       | 1         | Nice person. | 0         |
| 9  | Katty      | Perry       | http://127.0.0.1:8000/static/img/student-kp.jpg | 38   | 8       | null      | Nice person. | 0         |
| 10 | Will       | Smith       | http://127.0.0.1:8000/static/img/student-ws.jpg | 51   | 9       | 2         | Nice person. | 0         |
| 11 | Moderator  | null        | http://127.0.0.1:8000/static/img/person-1.jpg   | 6    | 9       | null      | null         | 0         |

#### courses_course:
| id | name                        | category         | photo                                         | description | credits | duration | lector            | slug       | start_date |
|----|-----------------------------|------------------|-----------------------------------------------|-------------|---------|----------|-------------------|------------|------------|
| 1  | HTML, CSS & JS              | Web Design       | http://127.0.0.1:8000/static/img/course-1.jpg | Nice course | 20      | 5        | Bob Harrison      | web-design | 24-11-20   |
| 2  | UI/UX Design CSS            | Graphic Design   | http://127.0.0.1:8000/static/img/course-2.jpg | Nice course | 10      | 3        | Jasmine Lucas     | web-design | 24-11-20   |
| 3  | Videos with Canva           | Video Editing    | http://127.0.0.1:8000/static/img/course-3.jpg | Nice course | 15      | 3        | Angelina Jolie    | web-design | 24-11-20   |
| 4  | Django Advanced             | Web Design       | http://127.0.0.1:8000/static/img/course-4.jpg | Nice course | 5       | 1        | Diyan Kalaydzhiev | web-design | 24-11-20   |
| 5  | PHP                         | Web Design       | http://127.0.0.1:8000/static/img/cat-3.jpg    | Nice course | 15      | 2        | <null>            | web-design | 24-11-20   |
| 6  | Drop-shipping. Online Sales | Online Marketing | http://127.0.0.1:8000/static/img/course.jpg   | Nice course | 30      | 8        | <null>            | web-design | 24-11-20   |

#### lessons_lesson:
| id | title                     | description  | readme                                                      | course_id |
|----|---------------------------|--------------|-------------------------------------------------------------|-----------|
| 1  | Introduction to HTML      | Nice course. | ['subject 1', '   subject 2  ', ' subject 3']               | 1         |
| 2  | Tags and elements in HTML | Nice course. | ['subject 4', '   subject 5  ', ' subject 6']               | 1         |
| 3  | CSS Basics. Classes & IDs | Nice course. | ['subject 7 ', ' subject 8', 'subject 9', 'subject 10', ''] | 1         |


## ----------------------------------------------------------------------------------------------------


## 4. Project architecture -> Apps:

### 4.1 Accounts (admin, lectors, students):
#### Models.py:
- [x] CustomUser (extends django default user -> AbstractBaseUser)
- [x] Profile (automatically created with 'signal' -> post_save)
#### Views.py:
- [x] UserRegisterPage
- [x] UserLoginPage
- [x] ProfileDetailsPage
- [x] ProfileCreateOrEditPage
- [x] ProfileDeletePage
#### Admin panel:
- [x] Register User model
- [x] Customize it:
  - [x] extend django base user -> UserAdmin
  - [x] list display
  - [x] ordering
  - [x] search functionality
  - [x] add fieldsets (categories)
  - [x] optional: integrate profile info in admin panel
  - [x] Attach Profile data (is_lector) beneath each User
#### Signals.py:
- [x] Upon USER creation, a PROFILE will be created too
#### Managers.py:
- [x] Custom user manager
#### Forms.py:
- [x] UserRegisterForm
- [x] UserEditForm
- [x] ProfileBaseForm
- [x] ProfileCreateOrEditForm
- [x] ProfileDeleteForm

### 4.2 Comments:
#### Models.py --> Comment
#### Views.py:
- [x] comment_add_view
- [x] CommentEditView
- [x] CommentDeleteView
#### Forms.py:
- [x] CommentBaseForm
- [x] CommentAddForm
- [x] CommentEditForm
- [x] CommentDeleteForm

### 4.3 Common:
#### Views.py:
- [x] HomePage
- [x] course_user_add
- [x] course_user_remove
- [x] lector_remove
- [x] AboutPage
- [x] AboutTeam
- [x] AboutStudents

### 4.4 Courses:
#### Models.py:
- [x] Course
#### Views.py:
- [x] CoursesCategoriesPage
- [x] CoursesAllPage
- [x] CoursesFromCategoryPage
- [x] CourseCreatePage
- [x] CourseDetailsPage
- [x] CourseEditPage
- [x] CourseDeletePage
#### Forms.py:
- [x] CourseBaseForm
- [x] CourseCreateForm
- [x] CourseEditForm
- [x] CourseDeleteForm

### 4.5 Gallery:
#### Models.py --> Album, Photos
#### Views.py:
- [x] AlbumsShowPage
- [x] AlbumAddPage
- [x] AlbumEditPage
- [x] AlbumDeletePage
- [x] PhotosShowPage
- [x] PhotoAddPage
- [x] PhotoDeletePage
#### Forms.py:
- [x] AlbumBaseForm
- [x] AlbumCreateForm
- [x] AlbumEditForm
- [x] AlbumDeleteForm
- [x] PhotoBaseForm
- [x] PhotoAddForm
- [x] PhotoEditForm
- [x] PhotoDeleteForm

### 4.6 Lessons:
#### Models.py --> Lesson
#### Views.py:
- [x] lesson_add_view
- [x] LessonEditView
- [x] LessonDeleteView
#### Forms.py:
- [x] LessonBaseForm
- [x] LessonAddForm
- [x] LessonDeleteForm

### 4.7 Library:
#### Models.py --> Book, Magazine
#### Views.py:
- [x] LibraryCategories
- [x] BooksPage
- [x] BookAddPage
- [x] BookDetailsPage
- [x] BookEditPage
- [x] BookDeletePage
- [x] MagazinesPage
- [x] MagazineAddPage
- [x] MagazineDetailsPage
- [x] MagazineEditPage
- [x] MagazineDeletePage
#### Forms.py:
- [x] BookBaseForm
- [x] BookAddForm
- [x] BookDeleteForm
- [x] MagazineBaseForm
- [x] MagazineAddForm
- [x] MagazineDeleteForm

### 4.8 Mixins:
- [x] Placeholder Mixin
- [x] ReadOnlyFields Mixin
- [x] DisabledFields Mixin

### 4.9 Validators:
- [x] Alphabetic name validator
- [x] Password validator
- [x] Capitalized name validator
