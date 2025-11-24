from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    data = {
        'name': 'Akash Sabu',
        'title': 'MCA Student | Aspiring Developer',
        'college': 'Rajagiri College of Social Sciences',
        'profile_image': 'images/profile.jpg',
        'bio': '''Passionate learner currently pursuing Master of Computer Applications (MCA) at Rajagiri College of Social Sciences, Kochi. 
                Completed BCA from St. Aloysius College, Mangaluru (2022–2025) with a strong foundation in programming (C, C#, Java, Python, R, SQL). 
                Actively expanding skills in Machine Learning, Generative AI, Cybersecurity, and Web Development. 
                Hobbies: Coding, reading tech books, and playing sports. 
                Driven by curiosity and the desire to build real-world solutions.''',

        'education': [
            {'degree': 'Master of Computer Applications (MCA)', 'institution': 'Rajagiri College of Social Sciences, Kochi', 'year': '2025 – 2027 (Pursuing)'},
            {'degree': 'Bachelor of Computer Applications (BCA)', 'institution': 'St. Aloysius College, Mangalore', 'year': '2022 – 2025'}
        ],

        'skills': [
            {'category': 'Programming Languages', 'items': ['Python', 'Java', 'C', 'C#', 'R Programming', 'SQL']},
            {'category': 'Web Technologies', 'items': ['HTML', 'CSS', 'JavaScript', 'Bootstrap']},
            {'category': 'Tools & Platforms', 'items': ['Git & GitHub', 'VS Code', 'Jupyter Notebook', 'MySQL']},
            {'category': 'Emerging Technologies', 'items': ['Machine Learning', 'Generative AI', 'Cybersecurity', 'Front-End Development']}
        ],

        'certifications': [
            {'name': 'Machine Learning', 'issuer': 'Simplilearn SkillUp', 'date': '08 Oct 2024', 'code': '7439267',
             'pdf': 'certificates/Machine-Learning.pdf'},
            {'name': 'Introduction to Front-End Development', 'issuer': 'Simplilearn SkillUp', 'date': '07 Oct 2024', 'code': '7436224',
             'pdf': 'certificates/Introduction-to-Front-End-Development.pdf'},
            {'name': 'Java Programming for Beginners', 'issuer': 'Simplilearn SkillUp', 'date': '08 Oct 2024', 'code': '7438136',
             'pdf': 'certificates/Java-Programming-for-Beginners.pdf'},
            {'name': 'Career Essentials in Generative AI', 'issuer': 'Microsoft and LinkedIn', 'date': '30 Apr 2025',
             'pdf': 'certificates/CertificateOfCompletion_Career Essentials in Generative AI by Microsoft and LinkedIn.pdf'},
            {'name': 'Career Essentials in Cybersecurity', 'issuer': 'Microsoft and LinkedIn', 'date': '16 Nov 2025',
             'pdf': 'certificates/CertificateOfCompletion_Career Essentials in Cybersecurity by Microsoft and LinkedIn.pdf'}
        ],

        'contact': 'akashsabu14@gmail.com',
        'github': 'https://github.com/AkashSabu-17',
        'linkedin': 'https://www.linkedin.com/in/akash-sabu'
    }
    return render_template('index.html', **data)

if __name__ == '__main__':
    app.run(debug=True)