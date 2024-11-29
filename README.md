# UniversityApp-November-2024-Project-Defence


## 1. Create project main architecture -> Apps:

### 1.1 Accounts (admin, lectors, students):
- 1.1.1 Models:
  - [x] User model (extend django default user -> AbstractBaseUser)
  - [x] Profile model

- 1.1.2 Views:
  - [x] Register view
  - [x] Login view
  - [x] Profile Details view
  - [x] Profile Edit view
  - [x] Profile Delete view

- 1.1.3 Admin panel
  - [x] Register User model
  - [x] Customize it:
    - [x] extend django base user -> UserAdmin
    - [x] list display
    - [x] ordering
    - [x] search functionality
    - [x] add fieldsets (categories)
    - [x] optional: integrate profile info in admin panel
    - [x] Attach Profile data (is_lector) beneath each User

- 1.1.4 Urls

- 1.1.5 Signals:
  - [x] Upon USER creation, a PROFILE will be created too

- 1.1.6 Managers:
  - [x] Custom user manager 

- 1.1.7 Forms:
  - [x] User Register Form
  - [x] User Edit Form
  - [x] Profile Edit Form
  - [x] Profile Delete Form

### 1.2 Common:
- 1.2.1 Models:
  - [x] Comment
  
- 1.2.2 Views: 
    - [x] Home page
    - [x] add user to course
    - [x] remove user from course
    - [x] admin remove lector from course
    - [ ] add comment view

- 1.2.3 Urls

- 1.2.1 Forms

### 1.3 Courses:
- [x] Models (Course model)
- [x] Views
  - [x] CoursesCategories view
  - [x] CoursesAll view
  - [x] CoursesFromCategory view
  - [x] CourseCreate view
  - [x] CourseDetails view
  - [x] CourseEdit view
  - [x] CourseDelete view
- [x] Urls
- [x] Forms
  - [ ] Course Base Form
  - [ ] Course Create Form
  - [ ] Course Edit Form
  - [ ] Course Delete Form

### 1.4 Online Classes:
- [ ] Models
- [ ] Views
- [ ] Urls
- [ ] Forms

### 1.5 UserPhotos:
- [ ] Models
- [ ] Views
- [ ] Urls
- [ ] Forms

### 1.6 UniversityPhotos:
- [ ] Models
- [ ] Views
- [ ] Urls
- [ ] Forms

### 1.7 Question & Answer Section:
- [ ] Models
- [ ] Views
- [ ] Urls
- [ ] Forms


## 3. Add validators for models:
- [x] Alphabetic name validator
- [x] Password validator
- [ ] Capitalized name validator


## 4. Add mixins:
- [x] Placeholder Mixin
- [x] ReadOnlyFields Mixin
- [x] DisabledFields Mixin


## 5. Create/import static files:
- [x] CSS
- [x] Images
- [x] Bootstrap & min.css
- [x] SCSS
- [x] JS Scripts


## 6. Create templates for the project:

### 6.1 Base html (header/meta + nav + {bl.content} + footer)
### 6.2 Index html (home)
### 6.3 Navbar html

### 6.4 Users (auth):
- [x] register
- [x] login

### 6.5 Profile:
- [x] profile create/edit
- [x] profile delete

### 6.6 Courses:
- [x] Courses (all)
- [x] Courses categories
- [x] Create course
- [x] Details course
- [x] Edit course
- [x] Delete course

### 6.7 Errors:
- [x] 403 Forbidden
- [x] 404 Page Not found
