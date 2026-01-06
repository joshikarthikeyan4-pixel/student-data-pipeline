import pandas as pd

# Load CSV files
students = pd.read_csv("data/students.csv")
courses = pd.read_csv("data/courses.csv")
enrollments = pd.read_csv("data/enrollments.csv")

# Sanity checks
print(students.head())
print(courses.head())
print(enrollments.head())

print("\nStudents info:")
print(students.info())

print("\nEnrollments info:")
print(enrollments.info())
student_enrollments = pd.merge(
    students,
    enrollments,
    on="student_id",
    how="inner"
)

print("\n=== STUDENT + ENROLLMENTS ===")
print(student_enrollments.head())
print(student_enrollments.info())
# Step 2B: (students + enrollments) ⨝ courses
final_df = pd.merge(
    student_enrollments,
    courses,
    on="course_id",
    how="left"
)
print("\n=== FINAL DATASET ===")
print(final_df.head())
print(final_df.info())

# Step 3A: Rename columns for clarity
final_df = final_df.rename(columns={
    "department_x": "student_department",
    "department_y": "course_department"
})

print("\n=== AFTER RENAMING COLUMNS ===")
print(final_df.head())

# Step 3B: Create passed column
final_df["passed"] = final_df["marks"] >= 50

print("\n=== AFTER ADDING PASSED COLUMN ===")
print(final_df[["student_id", "course_id", "marks", "passed"]].head())

# Step 3C: Save final dataset
output_path = "output/final_student_performance.csv"
final_df.to_csv(output_path, index=False)

print(f"\nFinal dataset saved to {output_path}")



