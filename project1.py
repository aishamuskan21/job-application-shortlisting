def shortlist_candidates():

    MIN_AGE = 21
    REQUIRED_QUALIFICATIONS = ["Bachelor's", "Master's", "PhD"]
    MIN_EXPERIENCE = 2

    shortlisted = []
    rejected = []

    print("Job Application Shortlisting Program")
    num_candidates = int(input("Enter the number of candidates: "))

    for i in range(num_candidates):
        print(f"\nEntering details for candidate {i + 1}")

        name = input("Enter candidate's name: ")
        age = int(input("Enter candidate's age: "))
        qualification = input("Enter candidate's qualification: ")
        experience = int(input("Enter candidate's years of experience: "))


        if (
            age >= MIN_AGE
            and qualification in REQUIRED_QUALIFICATIONS
            and experience >= MIN_EXPERIENCE
        ):
            shortlisted.append({"name": name, "age": age, "qualification": qualification, "experience": experience})
            print(f"{name} has been shortlisted.")
        else:
            rejected.append({"name": name, "age": age, "qualification": qualification, "experience": experience})
            print(f"{name} has been rejected.")

    print("\nSummary of Results")
    print("Shortlisted Candidates:")
    for candidate in shortlisted:
        print(f"- Name: {candidate['name']}, Age: {candidate['age']}, Qualification: {candidate['qualification']}, Experience: {candidate['experience']} years")

    print("\nRejected Candidates:")
    for candidate in rejected:
        print(f"- Name: {candidate['name']}, Age: {candidate['age']}, Qualification: {candidate['qualification']}, Experience: {candidate['experience']} years")

if __name__ == "__main__":
    shortlist_candidates()