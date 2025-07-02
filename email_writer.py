from transformers import pipeline

# Load the text generation pipeline
generator = pipeline("text-generation", model="distilgpt2")

print("🤖 Welcome to the Free Email Writer")

# Ask user for the email topic
prompt = input("📨 What should the email be about?\n> ")

# Use a prompt template to guide the model
email_prompt = f"""
Subject: Follow-up on our last conversation

Dear [Client Name],

I hope this message finds you well. I wanted to follow up regarding {prompt}. Please let me know if you have any updates or questions. I'm happy to assist further.

Best regards,
[Your Name]
"""

# Generate email text
result = generator(email_prompt, max_new_tokens=100, do_sample=True, truncation=True)

# Extract only the generated part after our prompt
generated_text = result[0]['generated_text'].replace(email_prompt, "").strip()

# Combine everything
final_email = email_prompt + generated_text

# Print the email
print("\n📧 Here's your email:\n")
print(final_email)

# Save to file
with open("generated_email.txt", "w", encoding="utf-8") as f:
    f.write(final_email)

print("\n✅ Email saved to 'generated_email.txt'")
