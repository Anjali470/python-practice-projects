# Create a function validate_password(password) that checks:
# 1. Minimum 8 characters
# 2. At least one uppercase letter
# 3. At least one lowercase letter
# 4. At least one digit
# 5. At least one special character (@, #, $, %, &, *)

# Return True if valid, False otherwise
# Also return specific error messages

# Example:
# validate_password("Hello123")
# Output: False, "Password must contain a special character"

# validate_password("Hello@123")
# Output: True, "Password is strong!"

password = "Anjali@1234"
def validate_password(password):

    special_characters = "!@#$%^&*"

    if len(password) < 8:
        return False, "Minimum 8 characters are required."

    if not any(ch.isupper() for ch in password):
        return False, "Atleast one uppercase letter is required."

    if not any(ch.islower() for ch in password):
        return False, "Atleast one lowercase letter is required."

    if not any(ch.isdigit() for ch in password):
        return False, "Atleast one digit is required."

    if not any(ch in special_characters for ch in password):
        return False, "Atleast one special character is required."

    return True, "Password is strong"

result = validate_password(password)

print(result[0], result[1])