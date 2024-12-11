# --DOCUMENTATION-- #

## 1. Project description:
#### This project aims to simulate a real university structure, principles and functionalities. It has courses with lessons and comments. Gallery with albums, containing university photos. Library with books & magazines. Users (students & lectors) can join, quit or manage (CRUD) a course, depending on their granted user permission.

## 2. Project requirements:
#### - Python version: 3.11.1 or higher
#### - db.sqlite3 (integrated in django, by default will be created after running initial migrations)
#### - Browser: Project has been developed and tested on Brave v1.73.97 Chromium 131.0.6778.108(official build, 64-bit)
#### - Working resolution: 1920x1080 fullHD (not mandatory, but recommended)

## 3. Setup instructions:
#### - Start a new (base) Django project on your PC (django system files, cores and functionalities in order to run a project)
#### - Clone project (get it on your PC):
```angular2html
git clone https://github.com/S7lkr/UniversityApp-November-2024
```
#### - Make sure 'venv' (virtual environment) is properly configured and installed. If not (in python console):
```angular2html
python -m venv venv
```

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
### Admin panel:
- [x] Register User model
- [x] Customize it:
  - [x] extend django base user -> UserAdmin
  - [x] list display
  - [x] ordering
  - [x] search functionality
  - [x] add fieldsets (categories)
  - [x] optional: integrate profile info in admin panel
  - [x] Attach Profile data (is_lector) beneath each User
### Signals.py:
- [x] Upon USER creation, a PROFILE will be created too
### Managers.py:
- [x] Custom user manager
### Forms.py:
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
