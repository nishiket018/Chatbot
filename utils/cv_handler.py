import fitz  # PyMuPDF

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Function to generate career insights based on resume content
def generate_career_insights(resume_text):
    # Basic keyword-based analysis (can expand with NLP or regex)
    skills = ["Python", "Data Analysis", "Machine Learning", "Project Management", "Data Science", "AI", "Leadership", "Communication", "Cloud Computing",
              "React", "Java", "JavaScript", "Frontend Development", "Backend Development", "Full Stack Development", "DevOps", "Cybersecurity", "SQL", "HTML", "CSS"]
    identified_skills = [skill for skill in skills if skill.lower() in resume_text.lower()]
    
    # Additional insights based on experience or education (this is just a mock-up, can be expanded further)
    experience_keywords = ["years of experience", "experience", "worked at", "leadership", "managed"]
    experience_mentioned = any(keyword.lower() in resume_text.lower() for keyword in experience_keywords)
    
    # Education-related keywords (if applicable)
    education_keywords = ["bachelor", "master", "phd", "university", "degree"]
    education_mentioned = any(keyword.lower() in resume_text.lower() for keyword in education_keywords)

    # Start of the insights message
    insights = "Based on your resume, here are some tailored career insights:\n\n"
    
    # Provide insights based on the identified skills
    if "Python" in identified_skills:
        insights += "- **Python** is a versatile skill. You could explore roles in **Data Science**, **Backend Development**, or **Software Engineering**.\n"
        insights += "  You may also want to consider learning **Python for Machine Learning** or **Data Engineering**.\n"
    
    if "Data Analysis" in identified_skills:
        insights += "- With **Data Analysis** skills, roles such as **Data Analyst**, **Business Intelligence Analyst**, or **Data Scientist** could be a good fit.\n"
        insights += "  A focus on **SQL**, **Excel**, and **Visualization Tools** like **Power BI** or **Tableau** can elevate your profile.\n"
    
    if "Machine Learning" in identified_skills:
        insights += "- Your **Machine Learning** expertise is highly valuable. Consider roles such as **Machine Learning Engineer**, **Data Scientist**, or **AI Researcher**.\n"
        insights += "  Familiarity with libraries like **TensorFlow** or **PyTorch** will help you stand out.\n"
    
    if "Project Management" in identified_skills:
        insights += "- If **Project Management** is a strength, you may want to explore roles like **Project Manager**, **Product Manager**, or **Scrum Master**.\n"
        insights += "  Familiarity with project management tools such as **JIRA**, **Asana**, or **Trello** can be beneficial.\n"
    
    if "Data Science" in identified_skills:
        insights += "- As someone with **Data Science** skills, roles such as **Data Scientist**, **Quantitative Analyst**, or **Data Engineer** are worth considering.\n"
        insights += "  Building expertise in **Deep Learning** or **Big Data Technologies** can increase your career prospects.\n"
    
    if "AI" in identified_skills:
        insights += "- Your experience in **AI** can lead to roles such as **AI Engineer**, **AI Researcher**, or **Automation Engineer**.\n"
        insights += "  It would be valuable to further develop expertise in **Natural Language Processing (NLP)** or **Computer Vision**.\n"
    
    if "Cloud Computing" in identified_skills:
        insights += "- Cloud computing is a growing field, with roles like **Cloud Engineer**, **Cloud Solutions Architect**, or **DevOps Engineer** becoming increasingly important.\n"
        insights += "  Familiarity with platforms like **AWS**, **Azure**, or **Google Cloud** would be highly advantageous.\n"
    
    # New insights for React, Java, and other popular fields
    
    if "React" in identified_skills:
        insights += "- **React** is a powerful JavaScript library for building user interfaces. You could consider roles such as **Frontend Developer**, **React Developer**, or **Full Stack Developer**.\n"
        insights += "  To enhance your React skills, learning about **Redux** (state management) and **React Router** (routing) would be beneficial.\n"
        insights += "  Familiarity with **Next.js** or **Gatsby** for server-side rendering or static site generation is a plus.\n"
    
    if "Java" in identified_skills:
        insights += "- **Java** remains a highly sought-after language, particularly for **Enterprise-level applications**. Roles such as **Java Developer**, **Software Engineer**, or **Backend Developer** would be suitable.\n"
        insights += "  Knowledge of frameworks like **Spring** and **Hibernate** will strengthen your Java development skills.\n"
        insights += "  Familiarity with **Microservices architecture** and tools like **Docker** or **Kubernetes** for containerization would add significant value.\n"
    
    if "JavaScript" in identified_skills:
        insights += "- **JavaScript** is essential for both **Frontend** and **Backend Development**. You could explore roles such as **Frontend Developer**, **Backend Developer**, or **Full Stack Developer**.\n"
        insights += "  Consider learning modern JavaScript frameworks like **Vue.js**, **Angular**, or **Node.js** for backend development.\n"
    
    if "Frontend Development" in identified_skills:
        insights += "- With a background in **Frontend Development**, you might pursue roles like **Frontend Developer**, **UI Developer**, or **UX/UI Designer**.\n"
        insights += "  Familiarity with **HTML**, **CSS**, **SASS**, and frontend frameworks like **Vue.js**, **React**, or **Angular** would be essential.\n"
    
    if "Backend Development" in identified_skills:
        insights += "- If you specialize in **Backend Development**, roles like **Backend Developer**, **API Developer**, or **Software Engineer** are great choices.\n"
        insights += "  Mastering **Node.js**, **Spring Boot**, **Django**, or **Flask** (Python) will enhance your backend development capabilities.\n"
    
    if "Full Stack Development" in identified_skills:
        insights += "- With **Full Stack Development** skills, you can take on roles like **Full Stack Developer**, **Software Engineer**, or **Technical Lead**.\n"
        insights += "  A good understanding of both frontend (React, Angular) and backend (Node.js, Spring) technologies is key.\n"
    
    if "DevOps" in identified_skills:
        insights += "- **DevOps** is critical for streamlining development and deployment pipelines. You could explore roles like **DevOps Engineer**, **Site Reliability Engineer**, or **Cloud Engineer**.\n"
        insights += "  Familiarity with **CI/CD pipelines**, **Docker**, **Kubernetes**, and cloud platforms like **AWS** or **Azure** would be highly valuable.\n"
    
    if "Cybersecurity" in identified_skills:
        insights += "- **Cybersecurity** is an ever-growing field. Roles like **Security Engineer**, **Penetration Tester**, or **Cybersecurity Analyst** would be a great fit.\n"
        insights += "  Consider learning about **network security**, **firewalls**, and certifications like **CISSP** or **CEH** to further your career.\n"
    
    # Providing experience-based insights
    if experience_mentioned:
        insights += "\nIt seems you have experience in the industry. Based on your experience level, consider the following steps:\n"
        insights += "- If you have a few years of experience, aim for mid-level positions such as **Senior Developer** or **Lead Data Analyst**.\n"
        insights += "- With more extensive experience, consider leadership positions like **Engineering Manager**, **Data Science Lead**, or **Product Director**.\n"
    
    # Providing education-based insights
    if education_mentioned:
        insights += "\nYour educational background can play a significant role in your career trajectory:\n"
        insights += "- If you have a **Bachelor’s** or **Master’s Degree**, you could target entry-level to mid-level roles in your field.\n"
        insights += "- A **PhD** could open up opportunities for specialized research roles or academic positions.\n"

    # If no specific skills are identified
    if not identified_skills:
        insights += "We couldn't identify any specific skills from your resume. Try to include more technical or soft skills, such as programming languages, leadership, or specific domain knowledge.\n"
    
    return insights
