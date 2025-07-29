# Permissions and Groups Setup

This project implements:
- Custom permissions (`can_view`, `can_create`, `can_edit`, `can_delete`) for the `Article` model.
- User groups:
  - **Editors**: can create and edit.
  - **Viewers**: can view only.
  - **Admins**: can do all actions.

### How to Test
1. Create users and assign them to groups via Django Admin.
2. Try accessing views protected by `@permission_required` decorators.
3. Verify each group’s access matches its permissions.
