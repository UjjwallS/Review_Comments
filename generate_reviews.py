import pandas as pd
import openai

# Set your OpenAI API key directly
openai.api_key = "sk-proj-REPLACE_ME_IF_NEEDED"

# Load product data
input_file = "_Products_Master__202505021131.csv"
df = pd.read_csv(input_file)

# Function to generate review
def generate_review(row):
    prompt = (
        f"Write a realistic customer review for the following product:\n"
        f"Product Name: {row['Product']}\n"
        f"Description: {row['Product Description']}\n"
        f"Type: {row['Product Type']}\n"
        f"Category: {row['Product Category']}"
    )
    print(f"Generating review for: {row['Product']}")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=100
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"OpenAI Error: {e}")
        return f"Error: {str(e)}"

# Generate reviews
print("Generating reviews for all products...")
df["Generated Review"] = df.apply(generate_review, axis=1)

# Save output
output_file = "Products_With_Reviews.csv"
df.to_csv(output_file, index=False)
print(f"Done! Reviews saved to: {output_file}")
