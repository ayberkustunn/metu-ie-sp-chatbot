"""
Knowledge Base for METU IE Summer Practice Chatbot.
All content is extracted from: https://sp-ie.metu.edu.tr/en
Last verified: March 2026
"""

KNOWLEDGE_CHUNKS = [
    # ── General Information ──────────────────────────────────────────────
    {
        "id": "gen-physical-attendance",
        "topic": "General Requirements",
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
        "page_title": "General Information",
        "content": (
            "Summer internships must be done by physically attending the work place. "
            "Remote or online internships are not accepted."
        ),
    },
    {
        "id": "gen-ie400-project-based",
        "topic": "IE 400 Project-Based Internship",
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
        "page_title": "General Information",
        "content": (
            "For IE 400, project based internships are allowed. Project based internship "
            "should be at least 6 weeks. Before the internship, you need to submit a "
            "proposal to the SP Committee which covers the content of the internship in "
            "detail. If the proposal is approved you can do the project based internship."
        ),
    },
    {
        "id": "gen-public-institutions",
        "topic": "Internships in Public Institutions",
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
        "page_title": "General Information",
        "content": (
            "Internships in public institutions: All public institutions in Turkey "
            "(Kamu kurumları) accept internship applications through a centralized system. "
            "Please consult the Career Gate portal (kariyerkapisi.cbiko.gov.tr) for further information."
        ),
    },
    {
        "id": "gen-erasmus",
        "topic": "Erasmus Internship",
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
        "page_title": "General Information",
        "content": (
            "Within the Erasmus program, it is possible to do an internship within the scope "
            "of Student Internship mobility. You may generally prefer an internship in Europe "
            "for a minimum of 3 months and a maximum of 12 months. For detailed information, "
            "please check the Erasmus office website at ico.metu.edu.tr. If the summer "
            "internships completed within the scope of this program are made for a short term "
            "(3 months), it can only be counted as one of IE300 and IE400 internship."
        ),
    },
    # ── SGK Insurance ────────────────────────────────────────────────────
    {
        "id": "sgk-system",
        "topic": "SGK Insurance Application System",
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
        "page_title": "General Information",
        "content": (
            "SGK Insurance Applications will be followed via METU OpenCourseWare platform (OCW) "
            "at ocw.metu.edu.tr. The insurance application module in the OCW system is now open. "
            "All 1st, 2nd, 3rd, and 4th year students are registered to the 'IE300/400 Summer "
            "Internship' course by default. The OCW course is created only for the practical "
            "purpose of collecting the insurance application information. This is not a real course. "
            "When your internship is over, you still need to get registered for IE300 or IE400 "
            "in the Fall semester (or summer school)."
        ),
    },
    {
        "id": "sgk-when-to-apply",
        "topic": "SGK Insurance - When to Apply",
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
        "page_title": "General Information",
        "content": (
            "The ideal moment to apply for the SGK insurance using OCW is 2-3 weeks before the "
            "beginning of your internship. On the Monday morning of each week, insurance "
            "applications of students beginning their internships within two weeks will be "
            "sent to Rektörlük. You should leave a safety margin of 1 whole week (Monday to "
            "Friday) between your application and the beginning of your SP. Do not apply too "
            "early (e.g. 2 months before) because Rektörlük does not process applications "
            "starting more than two weeks out. Do not apply too late (e.g. 5 days before) "
            "as this may cause delays."
        ),
    },
    {
        "id": "sgk-how-to-apply",
        "topic": "SGK Insurance - How to Apply",
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
        "page_title": "General Information",
        "content": (
            "To apply for SGK insurance: 1) Login to ocw.metu.edu.tr with your student account. "
            "2) Click on IE 300/400 course and find 'Required Information' in the course menu. "
            "3) Click on 'SGK Insurance Application' and fill in the questionnaire with your "
            "identity and company information. Click 'Submit Questionnaire' when finished. "
            "4) Upload your 'Declaration Form for students with/without family health insurance' "
            "to the OCW system (form available under Documents/Forms on SP website). "
            "5) You will NOT receive any notification when application is sent to Rektörlük. "
            "6) Your SGK insurance document will be available on e-devlet (turkiye.gov.tr) "
            "typically 2-3 workdays before the beginning of your SP."
        ),
    },
    {
        "id": "sgk-edevlet",
        "topic": "SGK Document on e-Devlet",
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
        "page_title": "General Information",
        "content": (
            "To access your SGK document on e-devlet: Login to turkiye.gov.tr. Type 'işe giriş' "
            "in the search field. Select '4A İşe Giriş Çıkış Bildirgesi (Sosyal Güvenlik Kurumu)'. "
            "Find the line corresponding to your current SP and click 'Belge oluştur'. "
            "The SP committee does not send SGK documents by email; they are available on e-devlet."
        ),
    },
    {
        "id": "sgk-emergency",
        "topic": "SGK Emergency Applications",
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
        "page_title": "General Information",
        "content": (
            "Emergency SGK applications: If your internship starts soon and you could not apply "
            "via OCW on time, fill in the excel file provided on the SP website with your "
            "internship information. Email the document to ie-staj@metu.edu.tr with the subject "
            "line: 'SGK basvurusu: Name Surname dd.mm.2025' providing your name and the beginning "
            "date of your SP. You should only use this emergency solution if you have a very valid reason."
        ),
    },
    {
        "id": "sgk-mistakes",
        "topic": "SGK Application - Fixing Mistakes",
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
        "page_title": "General Information",
        "content": (
            "If you made a mistake in your SGK Insurance Application questionnaire: First check "
            "if your application has already been sent to Rektörlük (applications are sent Monday "
            "mornings for SPs starting within two weeks). If NOT sent yet: enter a new questionnaire "
            "with correct info; the most recently filled version will be used and older versions "
            "ignored. If ALREADY sent: contact SP committee at ie-staj@metu.edu.tr. "
            "If your internship is cancelled: contact ie-staj@metu.edu.tr. "
            "If your SP begins the next workday and SGK document is not on e-devlet yet: contact "
            "SP Committee in the morning."
        ),
    },
    {
        "id": "sgk-voluntary",
        "topic": "Voluntary Internship SGK Insurance",
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
        "page_title": "General Information",
        "content": (
            "If you intend to do a voluntary internship, you can also get SGK insurance. "
            "Voluntary internships are not mandatory and not asked by the department. You don't "
            "need a letter from the committee for voluntary internships. METU provides SGK "
            "insurance for up to one month for one company. Use the same OCW procedure for a new "
            "SGK application, but make sure to send your second application only once the first "
            "SGK document is already issued. Rektörlük recommends leaving at least one blank day "
            "between two SPs. IMPORTANT: Foreign students are NOT allowed to do voluntary "
            "internships in Turkey; a work permit is required."
        ),
    },
    # ── Paid Summer Practices ────────────────────────────────────────────
    {
        "id": "paid-sp",
        "topic": "Paid Summer Practice Instructions",
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
        "page_title": "General Information",
        "content": (
            "If you did your SP in a private company in Turkey and received payment, you must: "
            "1) Login to ocw.metu.edu.tr. 2) Fill in the 'Paid SP form questionnaire' under "
            "IE300/400 course carefully (incomplete submissions are rejected by Rektörlük). "
            "3) Download, print, and sign the Paid Summer Practice Form (İşsizlik Fonu Katkısı "
            "Bilgi Formu), upload the scanned copy in PDF. 4) Upload the bank receipt showing "
            "payment from the company. If you made a mistake, submit a new form; the latest "
            "submission is used. If you did not receive payment or did SP in a public institution, "
            "ignore this section."
        ),
    },
    # ── Steps to Follow ──────────────────────────────────────────────────
    {
        "id": "steps-before-sp",
        "topic": "Steps Before Summer Practice",
        "source_url": "https://sp-ie.metu.edu.tr/en/steps-follow",
        "page_title": "Steps to Follow",
        "content": (
            "Before starting your SP: 1) Read the Summer Practice Manual (under Documents/Forms "
            "tab on SP website). 2) Check additional info about paid insurance or SGK insurance on "
            "the website. 3) Find a company for summer practice — you may check the list of "
            "companies that contacted the department, use social skills/family/friends, or examine "
            "past SP databases. 4) Some companies request a letter from the department explaining "
            "the aim and minimum duration of the internship and stating METU will pay insurance. "
            "5) Some companies may request an SP protocol (sözleşme/contract) form; see sample "
            "agreement under Documents/Forms. Leave the filled form at Undergraduate Secretary "
            "Office and pick it up signed in one week. 6) Apply for SGK insurance on time."
        ),
    },
    {
        "id": "steps-during-sp",
        "topic": "Steps During Summer Practice",
        "source_url": "https://sp-ie.metu.edu.tr/en/steps-follow",
        "page_title": "Steps to Follow",
        "content": (
            "During your SP: On the first day, submit the introduction letter from the SP "
            "committee to your supervisor. Attend work with full concentration, observe and "
            "participate. Take regular notes for your final report. Prepare a draft version "
            "while conducting practice. Towards the end, have the SP notebook signed and "
            "evaluation form filled by your supervisor."
        ),
    },
    {
        "id": "steps-after-sp",
        "topic": "Steps After Summer Practice",
        "source_url": "https://sp-ie.metu.edu.tr/en/steps-follow",
        "page_title": "Steps to Follow",
        "content": (
            "After your SP: 1) Your SP supervisor sends the 'SP Evaluation Form' and 'Employer "
            "Survey' to sp-belge@metu.edu.tr (can be signed traditionally or digitally, also "
            "possible to send by post in a closed envelope). 2) If you received payment in a "
            "private company, fill the Paid SP Questionnaire on OCW and upload required documents. "
            "3) Prepare your report following the Summer Practice Manual. 4) Register for IE 300 "
            "or IE 400 during registration period. 5) SP reports will be collected via ODTUClass "
            "(deadline announced there — strict deadline). Report must be in PDF format."
        ),
    },
    {
        "id": "steps-grading",
        "topic": "SP Report Grading Process",
        "source_url": "https://sp-ie.metu.edu.tr/en/steps-follow",
        "page_title": "Steps to Follow",
        "content": (
            "Your SP report will be graded by the faculty members assigned to your report. "
            "In the last month of the semester, reports requiring corrections will be returned "
            "to students. If your report is returned, you have 2-3 weeks to complete the "
            "requested corrections. Return the corrected report to the evaluating faculty "
            "via ODTUClass. Contact the faculty by email to learn the status of your report."
        ),
    },
    # ── Documents & Forms ────────────────────────────────────────────────
    {
        "id": "forms-overview",
        "topic": "Available Documents and Forms",
        "source_url": "https://sp-ie.metu.edu.tr/en/forms",
        "page_title": "Documents/Forms",
        "content": (
            "The following documents are available under the Documents/Forms section of the SP "
            "website: SP Meeting Presentations/Slides, Summer Practice Application Letters, "
            "SP Application Forms (IE-300 and IE-400 in Turkish and English, PDF and DOC), "
            "Sample Agreement Form (Sözleşme), Declaration Form for family health insurance, "
            "Paid Summer Practice Information Form (İşsizlik Fonu Katkısı Bilgi Formu), "
            "SP Evaluation Form and Employer Survey (Turkish and English versions), "
            "SP Manuals (IE300 Manual, IE400 Manufacturing Manual, IE400 Service Manual)."
        ),
    },
    {
        "id": "forms-application",
        "topic": "Summer Practice Application Forms",
        "source_url": "https://sp-ie.metu.edu.tr/en/summer-practice-application-form-staj-basvuru-belgesi",
        "page_title": "SP Application Form",
        "content": (
            "Summer Practice Application Forms are available for download from the SP website. "
            "IE-300 SP Application Form is available in Turkish and English (PDF and DOC). "
            "IE-400 SP Application Form is available in Turkish and English (PDF and DOC). "
            "Fill the form and send it to ie-staj@metu.edu.tr."
        ),
    },
    {
        "id": "forms-manuals",
        "topic": "Summer Practice Manuals",
        "source_url": "https://sp-ie.metu.edu.tr/en/forms",
        "page_title": "Documents/Forms",
        "content": (
            "Three SP manuals are available under Documents/Forms: "
            "1) IE300 Summer Practice Manual — covers requirements and guidelines for IE 300. "
            "2) IE400 Summer Practice Manufacturing Manual — for manufacturing-focused IE 400. "
            "3) IE400 Summer Practice Service Manual — for service-sector IE 400 practice. "
            "The manuals contain the questions you need to answer and report guidelines."
        ),
    },
    {
        "id": "forms-contract",
        "topic": "Summer Practice Contract (Sözleşme)",
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
        "page_title": "General Information",
        "content": (
            "If you need your SP work contract (staj sözleşmesi) to be signed, please leave it "
            "to the Undergraduate Secretary Office, IE 129, and get it back in one week."
        ),
    },
    # ── FAQ ───────────────────────────────────────────────────────────────
    {
        "id": "faq-arrange-company",
        "topic": "How to Find a Company for SP",
        "source_url": "https://sp-ie.metu.edu.tr/en/faq",
        "page_title": "FAQ",
        "content": (
            "There are two alternatives to arrange a summer practice organization: either apply "
            "to organizations personally or wait for summer practice opportunities announced by "
            "the department. The second option is more risky and capacity is usually very limited. "
            "If a firm requires the department to determine candidates, an announcement is made "
            "and students must send transcripts, resumes, and fill out the Preference Form under "
            "Forms. If assigned through the department, it is mandatory to do SP at that company."
        ),
    },
    {
        "id": "faq-departments-to-visit",
        "topic": "Which Departments to Visit During SP",
        "source_url": "https://sp-ie.metu.edu.tr/en/faq",
        "page_title": "FAQ",
        "content": (
            "It is preferable to take an all-around trip in the organization. You can gather "
            "observations through effective communication even if stationed at a particular "
            "department. You should inquire about overall operations."
        ),
    },
    {
        "id": "faq-topics",
        "topic": "Topics Studied During SP",
        "source_url": "https://sp-ie.metu.edu.tr/en/faq",
        "page_title": "FAQ",
        "content": (
            "Industrial engineering has a broad application area — its main field is systems run "
            "by people for the needs of others. Summer practice is your first lengthy period of "
            "observing and inquiring about systems in operation. Try to relate your courses to "
            "what you experience. Learn about various ways of getting organizational and technical "
            "functions performed. Use your Summer Practice Manual as a guide."
        ),
    },
    {
        "id": "faq-bank-ie400",
        "topic": "IE 400 Practice in a Bank",
        "source_url": "https://sp-ie.metu.edu.tr/en/faq",
        "page_title": "FAQ",
        "content": (
            "For IE 400, you should focus on the systems aspects (organizational, information, "
            "procedural, managerial) in a bank's service provision. Divisions or branches are "
            "suitable as they consist of integrated operation of people, financial resources, "
            "processes and information with performance expectations and ongoing decision making."
        ),
    },
    {
        "id": "faq-registration-paperwork",
        "topic": "Paperwork for SP Registration",
        "source_url": "https://sp-ie.metu.edu.tr/en/faq",
        "page_title": "FAQ",
        "content": (
            "Four steps to get officially registered for summer practice: "
            "1) Add IE 300/IE 400 course during registration at beginning of semester. "
            "2) Submit SP reports to Student Affairs Secretary (Room IE 128) within first two "
            "weeks of following academic term; also submit soft copy through the website under Forms. "
            "3) The company should send filled and signed evaluation form and employer survey to "
            "Student Affairs Secretary. "
            "4) Fill out the online questionnaire (will be announced)."
        ),
    },
    {
        "id": "faq-ie400-problem-definition",
        "topic": "IE 400 Problem Definition Requirements",
        "source_url": "https://sp-ie.metu.edu.tr/en/faq",
        "page_title": "FAQ",
        "content": (
            "A sufficient IE problem definition for IE 400 is described in Appendix A of the "
            "IE 400 Summer Practice Manual. You must supply your own description of problem "
            "formulation components and justify your points. Be specific to your practice "
            "organization. Problem identification should result from methodical analysis. "
            "Alternative courses of action and constraining factors should be supported by facts."
        ),
    },
    {
        "id": "faq-service-manufacturing",
        "topic": "Service Organization vs Manufacturing Questions",
        "source_url": "https://sp-ie.metu.edu.tr/en/faq",
        "page_title": "FAQ",
        "content": (
            "If your practice is in a service organization, see the analogies with manufacturing: "
            "a budget allocation might substitute a production plan, pre-classified records may "
            "stand as inventory, timetables for professionals can be counted as schedules, "
            "form flow may replace material flow. Highlight the reasons for such similarities."
        ),
    },
    {
        "id": "faq-multiple-students",
        "topic": "Multiple Students at Same Organization",
        "source_url": "https://sp-ie.metu.edu.tr/en/faq",
        "page_title": "FAQ",
        "content": (
            "Every student must have a separate report. For IE 400, the general outlook can be "
            "common. However, choose separate examples for observations. IE 400 report has two "
            "parts: questions and problem definition/project. Questions part must be different "
            "for each student. Problem definitions must always be different. The project part "
            "may be the same if complex (valid for at most two students). Students doing project "
            "type IE 400 can prepare either a regular report or a project type report."
        ),
    },
    {
        "id": "faq-ie400-project",
        "topic": "IE 400 Project Type Internship Details",
        "source_url": "https://sp-ie.metu.edu.tr/en/faq",
        "page_title": "FAQ",
        "content": (
            "IE 400 practice may involve a project type study (minimum 30 workdays / 6 weeks). "
            "Students must submit a two-page project proposal including brief company description "
            "and project details. The proposal must be approved (signed) by the company and "
            "submitted to the SP committee by the first week of SP. The committee evaluates "
            "validity. The report must describe all phases: the issue, organizational environment, "
            "data collected, tools used, outcomes, and implementation."
        ),
    },
    {
        "id": "faq-ie400-service-manual",
        "topic": "IE 400 Service Manual Availability",
        "source_url": "https://sp-ie.metu.edu.tr/en/faq",
        "page_title": "FAQ",
        "content": (
            "Yes, an IE 400 Summer Practice Manual for service sector is available. "
            "It can be found under the Documents/Forms section on the SP website."
        ),
    },
    # ── SP Committee ─────────────────────────────────────────────────────
    {
        "id": "committee-contact",
        "topic": "SP Committee Contact Information",
        "source_url": "https://sp-ie.metu.edu.tr/en/sp-committee",
        "page_title": "SP Committee",
        "content": (
            "The SP Committee can be contacted via email at ie-staj@metu.edu.tr. "
            "Fax: +90 (312) 210 4786. For evaluation form and employer survey submissions, "
            "the email is sp-belge@metu.edu.tr. Physical documents can be left at the "
            "Undergraduate Secretary Office, IE 129. Before emailing, check the SP website "
            "and meeting slides for answers to your questions."
        ),
    },
    # ── SP Opportunities ─────────────────────────────────────────────────
    {
        "id": "sp-opportunities",
        "topic": "Summer Practice Opportunities",
        "source_url": "https://sp-ie.metu.edu.tr/en/sp-opportunities",
        "page_title": "SP Opportunities",
        "content": (
            "The department posts available summer practice opportunities on the SP website "
            "under the 'SP Opportunities' tab. Students can check for companies that contacted "
            "the department seeking summer practice students. There is also a 'Previous SP "
            "Opportunities' section for reference. Capacity is usually very limited."
        ),
    },
    # ── Meeting / Announcements ──────────────────────────────────────────
    {
        "id": "meeting-2025",
        "topic": "SP Meeting 2025",
        "source_url": "https://sp-ie.metu.edu.tr/en",
        "page_title": "Home",
        "content": (
            "A general meeting on IE 300 - IE 400 summer internship courses and SP procedures "
            "was held on March 14, 2025, at 14:40 in IE03 for IE300 and IE04 for IE400. "
            "The slides of the meeting can be found under the Documents/Forms section."
        ),
    },
    # ── IE 300 vs IE 400 Overview ────────────────────────────────────────
    {
        "id": "ie300-overview",
        "topic": "IE 300 Summer Practice Overview",
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
        "page_title": "General Information",
        "content": (
            "IE 300 is the first mandatory summer practice course for IE students. "
            "A minimum of 20 workdays (4 weeks) of summer practice is required. "
            "Students must physically attend the workplace. The IE 300 Summer Practice "
            "Manual (available under Documents/Forms) guides the report writing process. "
            "After completing the practice, students register for IE 300 in the following "
            "semester and submit their reports via ODTUClass."
        ),
    },
    {
        "id": "ie400-overview",
        "topic": "IE 400 Summer Practice Overview",
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
        "page_title": "General Information",
        "content": (
            "IE 400 is the second mandatory summer practice course. It requires observing "
            "and analyzing a purposeful system in real life. The report has two parts: "
            "questions and problem definition/project. There are separate manuals for "
            "manufacturing and service settings. Project-based IE 400 internships are "
            "allowed (minimum 6 weeks) with prior proposal approval from the SP Committee."
        ),
    },
]

# ── Curated FAQ — common student questions with direct answers ──────────
CURATED_FAQ = [
    {
        "question": "How long is the summer practice?",
        "answer": (
            "IE 300 requires a minimum of 20 workdays (4 weeks). IE 400 also requires "
            "a minimum of 20 workdays (4 weeks) for regular internships, or 30 workdays "
            "(6 weeks) for project-based internships. Please check the SP manuals for details."
        ),
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
    },
    {
        "question": "Who do I contact for SP questions?",
        "answer": (
            "Contact the SP Committee at ie-staj@metu.edu.tr. For evaluation form and "
            "employer survey submissions, use sp-belge@metu.edu.tr. Fax: +90 (312) 210 4786. "
            "Please check the website and meeting slides before emailing."
        ),
        "source_url": "https://sp-ie.metu.edu.tr/en/sp-committee",
    },
    {
        "question": "Can I do my summer practice abroad?",
        "answer": (
            "Yes. You can do your SP abroad. If doing it through the Erasmus program, it "
            "can count as either IE300 or IE400 (a 3-month Erasmus internship counts for "
            "only one of IE300/IE400). Check the Erasmus office at ico.metu.edu.tr for details."
        ),
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
    },
    {
        "question": "Can I do summer practice online or remotely?",
        "answer": (
            "No. Summer internships must be done by physically attending the workplace. "
            "Remote or online internships are not accepted."
        ),
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
    },
    {
        "question": "Where do I submit my SP report?",
        "answer": (
            "SP reports are collected via ODTUClass. The deadline will be announced on "
            "ODTUClass and it is a strict deadline. Reports must be in PDF format. "
            "You must register for IE300 or IE400 during the registration period."
        ),
        "source_url": "https://sp-ie.metu.edu.tr/en/steps-follow",
    },
    {
        "question": "How do I get an SP letter from the department?",
        "answer": (
            "Some companies request a letter explaining the internship aim, minimum duration, "
            "and confirming METU pays insurance. Download the SP Application Form from the "
            "Documents/Forms tab, fill it, and send to ie-staj@metu.edu.tr."
        ),
        "source_url": "https://sp-ie.metu.edu.tr/en/steps-follow",
    },
    {
        "question": "What if I get paid during my summer practice?",
        "answer": (
            "If paid by a private company in Turkey: fill the 'Paid SP form questionnaire' "
            "on OCW, upload signed Paid SP Form and bank receipt. If unpaid or at a public "
            "institution, no action needed for paid SP forms."
        ),
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
    },
    {
        "question": "Can foreign students do voluntary internships?",
        "answer": (
            "No. Foreign students are NOT allowed to do voluntary internships in Turkey. "
            "A work permit is required for voluntary internships."
        ),
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
    },
]
