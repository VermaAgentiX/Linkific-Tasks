export function validateStudent(values) {
  const errors = {};
  const name = values.name.trim();
  const course = values.course.trim();
  const email = values.email.trim();
  const age = String(values.age).trim();

  if (!name) errors.name = "Full name is required.";
  else if (name.length < 2) errors.name = "Name must be at least 2 characters.";
  else if (name.length > 80) errors.name = "Name cannot exceed 80 characters.";
  else if (!/^[A-Za-z][A-Za-z .'-]*$/.test(name)) errors.name = "Use letters, spaces, apostrophes, periods, or hyphens.";

  if (!age) errors.age = "Age is required.";
  else if (!/^\d+$/.test(age) || Number(age) < 1 || Number(age) > 120) errors.age = "Enter a whole number from 1 to 120.";

  if (!course) errors.course = "Course is required.";
  else if (course.length < 2) errors.course = "Course must be at least 2 characters.";
  else if (course.length > 100) errors.course = "Course cannot exceed 100 characters.";

  if (!email) errors.email = "Email address is required.";
  else if (email.length > 254 || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) errors.email = "Enter a valid email address.";

  return errors;
}

export function validateRegistration({ name, email, password }) {
  const errors = {};
  if (!name.trim()) errors.name = "Full name is required.";
  else if (name.trim().length < 2) errors.name = "Name must be at least 2 characters.";
  else if (!/^[A-Za-z][A-Za-z .'-]*$/.test(name.trim())) errors.name = "Use letters, spaces, apostrophes, periods, or hyphens.";
  if (!email.trim()) errors.email = "Email address is required.";
  else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.trim())) errors.email = "Enter a valid email address.";
  if (!password) errors.password = "Password is required.";
  else if (password.length < 8) errors.password = "Password must be at least 8 characters.";
  else if (password.length > 128) errors.password = "Password cannot exceed 128 characters.";
  else if (!password.trim()) errors.password = "Password cannot contain only spaces.";
  return errors;
}

export function firstApiError(error) {
  if (error?.fieldErrors) {
    const first = Object.values(error.fieldErrors)[0];
    if (first) return first;
  }
  return error?.message || "Something went wrong. Please try again.";
}
