# UniversityApp-November-2024-Project-Defence:

## 1. Create apps:

- [x] Accounts app (admin, lectors, students)
- [ ] Common app
- [ ] Lectors app
- [ ] Students app
- [ ] PersonPhotos app
- [x] Courses app
- [ ] OnlineLectures app
- [ ] UniversityPhotos app

## 2. Create models:

- [x] Accounts app:
    - [x] User model
    - [x] Profile model
- [ ] Common app:
    - [ ] Comment model
    - [ ] Like model
- [ ] Lector model
- [ ] Student model
- [ ] PersonPhoto model
- [x] Course model
- [ ] OnlineLecture model
- [ ] UniversityPhoto model

## 3. Make migrations and migrate to DB:

- [x] Accounts app:
    - [x] User model
    - [x] Profile model
- [ ] Common app:
    - [ ] Comment model
    - [ ] Like model
- [ ] Lector model
- [ ] Student model
- [ ] PersonPhoto model
- [x] Course model
- [ ] OnlineLecture model
- [ ] UniversityPhoto model

## 4. Add validators for models:

- [x] Alphabetic name validator
- [x] Password validator
- [ ] Capitalized name validator

## 5. Add mixins:

- [x] Placeholder Mixin
- [x] ReadOnlyFields Mixin
- [x] DisabledFields Mixin

## 5. Create forms:
- [ ] Auth:
  - [x] Register form
  - [x] Login form
- [ ] Courses:
  - [x] Create Course Form
  - [x] Edit Course Form
  - [x] Delete Course Form


## 6. Register UserModel in admin panel:
- [x] Customize it:
    - [x] extend django base user -> UserAdmin
    - [x] list display
    - [x] ordering
    - [x] search functionality
    - [x] add fieldsets (categories)
    - [ ] optional: integrate profile info in admin panel

## 7. Create and implement templates (html-s):

- [x] base
- [x] home
- [x] register
- [x] login
- [x] courses
- [ ] online lectures
- [ ] lectors
- [ ] students
- [ ] other...


## 8. Create and implement static files:
- [x] CSS
- [x] Pictures


## 9. Create views:
- [x] Accounts views
    - [x] UserRegisterPage view
    - [x] UserLoginPage view
    - [ ] ProfileDetailsPage view
    - [ ] ProfileEditPage view
    - [ ] ProfileDeletePage view
- [ ] Common views
    - [ ] show home page
- [ ] Lectors views
    - [ ] create
    - [ ] details
    - [ ] edit
    - [ ] delete
- [ ] Students views
    - [ ] create
    - [ ] details
    - [ ] edit
    - [ ] delete
- [ ] PersonPhotos views
    - [ ] create
    - [ ] details
    - [ ] edit
    - [ ] delete
- [x] Courses views
    - [x] create
    - [x] details
    - [x] edit
    - [x] delete
- [ ] OnlineLectures views
    - [ ] create
    - [ ] details
    - [ ] edit
    - [ ] delete
- [ ] UniversityPhotos views
    - [ ] create
    - [ ] details
    - [ ] edit
    - [ ] delete