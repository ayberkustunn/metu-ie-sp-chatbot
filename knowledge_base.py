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
            "Summer practice attendance rules depend on the course and company type. "
            "IE 300 (manufacturing): must be fully face-to-face at the company/plant. "
            "IE 400 at a manufacturing company: must be fully face-to-face at the company/plant. "
            "IE 400 at a service company: can be face-to-face OR hybrid (face-to-face + online). "
            "Fully remote or fully online internships are not accepted for any summer practice."
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
        "id": "prerequisite-chain",
        "topic": "Prerequisite Chain for IE Courses",
        "source_url": "https://ie.metu.edu.tr/en/prerequisite-chain",
        "page_title": "Prerequisite Chain",
        "content": (
            "The prerequisite chain for METU IE courses can be found at "
            "ie.metu.edu.tr/en/prerequisite-chain. IE 300 (Summer Practice I) and "
            "IE 400 (Summer Practice II) are part of the undergraduate curriculum. "
            "Students should check the prerequisite chain to understand which courses "
            "must be completed before registering for IE 300 and IE 400. "
            "The full BS Industrial Engineering curriculum is available at "
            "ie.metu.edu.tr/en/bs-industrial-engineering-curriculum. "
            "The Turkish version of the curriculum is at "
            "ie.metu.edu.tr/tr/endustri-muhendisligi-lisans-ogretim-programi."
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
    # ── NEW: IE 300 / IE 400 Prerequisites (EXACT course lists) ─────────
    {
        "id": "prereq-ie300",
        "topic": "IE 300 Prerequisites - Exact Course List",
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
        "page_title": "IE 300 Introduction Slides 2025",
        "content": (
            "Prerequisites for IE 300 (Summer Practice I): "
            "You must have completed ALL of the following with a grade of DD or above: "
            "1) IE 102, "
            "2) IE 251, IE 265, IE 241, OHS 101 (fall semester courses), "
            "3) At least one course from the set {IE 266, IE 252} (spring semester courses). "
            "If any one of the prerequisite courses is not completed with a grade of DD or "
            "above, you cannot register for IE 300. "
            "The full prerequisite chain is available at ie.metu.edu.tr/en/prerequisite-chain"
        ),
    },
    {
        "id": "prereq-ie400",
        "topic": "IE 400 Prerequisites - Exact Course List",
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
        "page_title": "IE 400 Introduction Slides 2025",
        "content": (
            "Prerequisites for IE 400 (Summer Practice II): "
            "You must have completed ALL of the following with a grade of DD or above: "
            "1) IE 300 (Summer Practice I must be completed first), "
            "2) IE 252, IE 323, IE 333, "
            "3) Any two courses from the set: {IE 304, IE 324, IE 372, IE 368}. "
            "If any one of the prerequisite courses is not completed with a grade of DD or "
            "above, IE 400 cannot be conducted. You must check the prerequisite chain at "
            "ie.metu.edu.tr/en/prerequisite-chain before planning your summer practice."
        ),
    },
    # ── NEW: IE 300 MANUFACTURING Requirement ────────────────────────────
    {
        "id": "ie300-company-type",
        "topic": "IE 300 Company Type - Manufacturing Required",
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
        "page_title": "IE 300 Introduction Slides 2025",
        "content": (
            "IE 300 summer practice MUST be done in a MANUFACTURING (production) company. "
            "Service-sector companies are NOT suitable for IE 300. "
            "Suitable manufacturing companies include: automotive parts, machine parts, "
            "electronics, furniture, textiles, consumer durables (refrigerator, washing machine), "
            "and similar production/manufacturing firms. "
            "Batch process industries are also accepted: steel, paper mills, pharmaceutical, "
            "food and beverages. Continuous process industries (cement, sugar, flour mill) are accepted. "
            "NOT accepted for IE 300: hospitals, hotels, banks, research organizations, "
            "transportation companies, cargo carriers, public institutions, NGOs, or any "
            "service-only organization. These are suitable for IE 400 only."
        ),
    },
    # ── NEW: IE 400 Company Type (manufacturing + service) ───────────────
    {
        "id": "ie400-company-type",
        "topic": "IE 400 Company Type - Manufacturing or Service",
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
        "page_title": "IE 400 Introduction Slides 2025",
        "content": (
            "IE 400 summer practice can be done in EITHER a manufacturing OR a service company. "
            "Suitable manufacturing firms: automotive, machine parts, electronics, furniture, "
            "textiles, consumer durables, steel, paper mills, pharmaceutical, food and beverages, "
            "cement, sugar, flour mills, and similar production firms. "
            "Suitable service organizations: hospitals, hotels, banks, research organizations "
            "(e.g. ODTU Teknokent), transportation and cargo companies, public institutions, "
            "non-governmental organizations (NGOs), and other service-sector firms. "
            "Use the IE 400 Manufacturing Manual if your company is manufacturing, "
            "or the IE 400 Service Manual if your company is in the service sector."
        ),
    },
    # ── NEW: IE 300 vs IE 400 Comparison ─────────────────────────────────
    {
        "id": "ie300-vs-ie400",
        "topic": "IE 300 vs IE 400 Comparison",
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
        "page_title": "General Information",
        "content": (
            "Comparison of IE 300 and IE 400: "
            "IE 300 (Summer Practice I): Must be done FIRST. Company must be MANUFACTURING only. "
            "Minimum 20 workdays (4 weeks). Report follows the IE 300 Manual. "
            "Graded out of 200 points for questions + style. "
            "IE 400 (Summer Practice II): Done AFTER IE 300 is completed. Company can be "
            "manufacturing OR service. Minimum 20 workdays (4 weeks) for regular internships, "
            "or minimum 30 workdays (6 weeks) for project-based internships. "
            "Report follows IE 400 Manufacturing Manual or IE 400 Service Manual. "
            "Report has two parts: Questions section (200 points) and Problem/Project section "
            "(100 points). You must pass both parts separately. "
            "IE 300 must be completed before you can do IE 400."
        ),
    },
    # ── NEW: Face-to-Face / Hybrid Rules ─────────────────────────────────
    {
        "id": "ie400-hybrid-rules",
        "topic": "IE 400 Face-to-Face and Hybrid Rules",
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
        "page_title": "IE 400 Introduction Slides 2025",
        "content": (
            "IE 400 attendance rules depend on the company type: "
            "If your IE 400 company is a MANUFACTURING company: your summer practice must "
            "be done totally in the company (plant), fully face-to-face. No hybrid or remote option. "
            "If your IE 400 company is a SERVICE company: your summer practice can be either "
            "face-to-face OR hybrid (face-to-face + online). "
            "Note: IE 300 must always be fully face-to-face in a manufacturing company, regardless. "
            "Fully remote/online internships are not accepted for either IE 300 or IE 400."
        ),
    },
    # ── NEW: Report Grading Criteria (IE 300) ────────────────────────────
    {
        "id": "grading-ie300",
        "topic": "IE 300 Report Grading Criteria",
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
        "page_title": "IE 300 Summer Practice Manual",
        "content": (
            "IE 300 report grading: The report is graded out of a total of 200 points. "
            "Point distribution: Introductory Features (10 pts), Analysis of the Macro Aspects "
            "(20 pts), An Overview of the Production System (35 pts), Production Planning and "
            "Control System (50 pts), Quality Planning and Control System (20 pts), "
            "Management Information System (20 pts), Observation of a Professional at Work (10 pts), "
            "Analysis of a Decision Making Problem (15 pts), Conclusion (10 pts), "
            "Style and Organization (10 pts). "
            "Any grade between 125 and 160 points, or any section grade less than 50% of the "
            "full score, will be considered Incomplete and the report will be returned for revision. "
            "A grade less than 125 points is considered Unsatisfactory and the summer practice "
            "must be repeated at a different company."
        ),
    },
    # ── NEW: Report Grading Criteria (IE 400) ────────────────────────────
    {
        "id": "grading-ie400",
        "topic": "IE 400 Report Grading Criteria",
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
        "page_title": "IE 400 Manufacturing Manual",
        "content": (
            "IE 400 report grading: The report has two separately graded sections. "
            "QUESTIONS SECTION (200 points total): Introductory Features (10 pts), "
            "Analysis of Macro Aspects (20 pts), Overview of Production System (35 pts), "
            "Production Planning and Control (50 pts), Quality Planning and Control (20 pts), "
            "Management Information System (20 pts), Work Study (20 pts), Conclusion (15 pts), "
            "Style and Organization (10 pts). "
            "PROBLEM/PROJECT SECTION (100 points total). "
            "You must pass BOTH sections separately. For the questions section: grades 125-160 "
            "or any section below 50% = Incomplete (returned for revision). Below 125 = "
            "Unsatisfactory (repeat SP at different company). "
            "For the problem/project section: grades 40-65 = Incomplete (revision). "
            "Below 40 = Unsatisfactory (repeat SP). "
            "PROJECT-TYPE REPORT grading (100 pts): Introduction (5), Company Description & "
            "Literature Review (10), Problem Definition (30), Data Gathering and Analysis (10), "
            "Solution Approaches (20), Results (15), Conclusion (10)."
        ),
    },
    # ── NEW: Questionnaire Requirement ───────────────────────────────────
    {
        "id": "questionnaire-requirement",
        "topic": "Mandatory Online Questionnaire",
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
        "page_title": "IE 300/400 Introduction Slides 2025",
        "content": (
            "Both IE 300 and IE 400 students must fill out the mandatory online questionnaire. "
            "The questionnaire is completed via METU Survey (the link will be shared by the SP "
            "Committee at the beginning of the semester when you register for IE 300/IE 400). "
            "The questionnaire must be filled out before the report submission deadline. "
            "If you do not fill out the questionnaire, your summer practice report will be "
            "considered INCOMPLETE regardless of the report quality. "
            "This is a separate requirement from the SGK insurance questionnaire on OCW."
        ),
    },
    # ── NEW: Plagiarism / AI Check ───────────────────────────────────────
    {
        "id": "plagiarism-check",
        "topic": "Plagiarism and AI Content Check",
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
        "page_title": "IE 400 Introduction Slides 2025",
        "content": (
            "SP reports are submitted through ODTUClass via a Turnitin assignment to check "
            "for plagiarism (intihal). The similarity score must be less than 20%. "
            "Reports are also checked for AI-generated content. "
            "Make sure your report is original work. You can use tools like Google Grammarly "
            "to correct grammar, but the content must be your own analysis and observations."
        ),
    },
    # ── NEW: Declaration Form Guidance ───────────────────────────────────
    {
        "id": "declaration-forms-guide",
        "topic": "Which Declaration Form to Use (Health Insurance)",
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
        "page_title": "General Information",
        "content": (
            "When applying for SGK insurance via OCW, you must upload a Declaration Form "
            "(Beyan ve Taahhütname). There are TWO versions — choose the correct one: "
            "1) 'Declaration Form for students WITH family health insurance' "
            "(Beyanname - Sağlık Hizmeti Alan): Use this if you are currently covered by "
            "your family's health insurance (Genel Sağlık Sigortası through a parent). "
            "2) 'Declaration Form for students WITHOUT family health insurance' "
            "(Beyanname - Sağlık Hizmeti Almayan): Use this if you do NOT have family health "
            "insurance coverage. "
            "Both forms are available under the Documents/Forms tab on the SP website. "
            "Download the correct form, fill it out, and upload the scanned/signed copy to OCW."
        ),
    },
    # ── NEW: SP Application Form - Separate Per Company ──────────────────
    {
        "id": "application-form-per-company",
        "topic": "SP Application Form - One Per Company",
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
        "page_title": "IE 400 Introduction Slides 2025",
        "content": (
            "You can apply to more than one company for summer practice. However, for EACH "
            "company you want to apply to, you must fill out a SEPARATE SP Application Form "
            "(Staj Başvuru Belgesi). Download the form from the SP website under Documents/Forms, "
            "fill it out with the specific company information, and submit it. "
            "Once accepted by a company, deliver the signed SP Application Form to the company "
            "along with other documents they require (CV, etc.)."
        ),
    },
    # ── NEW: Summer School Registration Option ───────────────────────────
    {
        "id": "summer-school-registration",
        "topic": "Registering for IE 300/400 in Summer School",
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
        "page_title": "IE 300/400 Introduction Slides 2025",
        "content": (
            "After completing your summer practice, you must register for IE 300 or IE 400 "
            "in the immediate following academic term. This is typically the Fall semester. "
            "However, you may also register for IE 300 or IE 400 during summer school "
            "if you attend summer school for some courses. "
            "If you attend summer school, the available time interval for the internship "
            "is reduced because summer school typically runs in July. Plan accordingly. "
            "Report deadlines and submission procedures are the same regardless of whether "
            "you register in Fall or summer school."
        ),
    },
    # ── NEW: SP Time Interval and Deadlines (with staleness warning) ─────
    {
        "id": "sp-time-interval",
        "topic": "SP Time Interval and Report Deadlines",
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
        "page_title": "General Information",
        "content": (
            "The summer practice is conducted during the summer period, typically spanning "
            "approximately 3 months (late June through late September). The exact dates "
            "may change each academic year, so always check the SP website and introduction "
            "slides for the current year's specific time interval. "
            "Report submission deadlines are announced on ODTUClass at the beginning of the "
            "registration semester. The deadline is typically within the first 4 weeks of "
            "the semester. This is a STRICT deadline — late submissions are not accepted. "
            "Always check ODTUClass for the exact due date for your specific academic year."
        ),
    },
    # ── NEW: Year-specific report deadlines from uploaded intro files ─────
    {
        "id": "deadline-ie300-2025-2026",
        "topic": "IE 300 Report Deadline — 2025-2026 Academic Year",
        "source_url": "local_file://ie300_introduction_2025-2.pdf",
        "page_title": "IE 300 Introduction Slides 2025-2026",
        "content": (
            "IE 300 report deadline for the 2025-2026 academic year: October 24, 2025. "
            "Source: IE 300 Introductory Session slides (2025-2026). "
            "After completing your summer practice in Summer 2025, you must register for "
            "IE 300 in the immediate following academic term (Fall 2025-2026). "
            "Reports are due within the first 4 weeks of that term. "
            "NOTE: This deadline is specific to the 2025-2026 academic year. "
            "For other years, check the introduction slides and ODTUClass for the updated due date."
        ),
    },
    {
        "id": "deadline-ie400-2025-2026",
        "topic": "IE 400 Report Deadline — 2025-2026 Academic Year",
        "source_url": "local_file://ie400_introduction_2025.pdf",
        "page_title": "IE 400 Introduction Slides 2025-2026",
        "content": (
            "IE 400 report deadline for the 2025-2026 academic year: October 24, 2025. "
            "Source: IE 400 Introductory Session slides (2025-2026). "
            "After completing your summer practice in Summer 2025, you must register for "
            "IE 400 in the immediate following academic term (Fall 2025-2026). "
            "Reports are due within the first 4 weeks of that term. "
            "NOTE: This deadline is specific to the 2025-2026 academic year. "
            "For other years, check the introduction slides and ODTUClass for the updated due date."
        ),
    },
    # ── NEW: IE 400 Report Structure ─────────────────────────────────────
    {
        "id": "ie400-report-structure",
        "topic": "IE 400 Report Structure and Sections",
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
        "page_title": "IE 400 Manufacturing Manual",
        "content": (
            "The IE 400 report must include: Table of Contents, Introduction, Main Body "
            "(answering manual questions), Conclusion, References, and Appendix. "
            "The report must be written in English. "
            "MANUFACTURING MANUAL sections: 1) Introductory Features, 2) Analysis of Macro "
            "Aspects, 3) Overview of Production System, 4) Production Planning and Control, "
            "5) Quality Planning and Control, 6) Management Information System, 7) Work Study, "
            "8) Conclusion. You must answer at least 3 questions from Chapter 4, at least 2 "
            "from Chapter 6, and at least 1 from each of Chapters 5 and 7. "
            "Plus: a Problem Definition or Participated Project section (see Appendix A/B). "
            "SERVICE MANUAL sections are analogous but adapted for service organizations. "
            "If a question is not applicable, provide a clear justification of why. "
            "Add a glossary of technical terms including company-specific jargon."
        ),
    },
    # ── NEW: IE 300 Report Structure ─────────────────────────────────────
    {
        "id": "ie300-report-structure",
        "topic": "IE 300 Report Structure and Sections",
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
        "page_title": "IE 300 Summer Practice Manual",
        "content": (
            "The IE 300 report must include: Table of Contents, Introduction, Main Body "
            "(answering manual questions), Conclusion, References, and Appendix. "
            "The report must be written in English. "
            "IE 300 MANUAL sections: 1) Introductory Features, 2) Analysis of Macro Aspects, "
            "3) Overview of Production System, 4) Production Planning and Control System, "
            "5) Quality Planning and Control System, 6) Management Information System, "
            "7) Observation of a Professional at Work, 8) Analysis of a Decision Making Problem, "
            "9) Conclusion. "
            "If a question is not applicable to your practice organization, provide a clear "
            "justification. You may modify a question to make it relevant and then answer it. "
            "Add a glossary of technical terms. Reports are due within the first weeks of the "
            "registered academic term via ODTUClass in PDF format."
        ),
    },
    # ── NEW: Company Insuring Student ────────────────────────────────────
    {
        "id": "company-insurance-option",
        "topic": "Company Providing Insurance Instead of METU",
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
        "page_title": "IE 400 Introduction Slides 2025",
        "content": (
            "The company where you do your summer practice can also insure you for the "
            "internship period. In that case, you are NOT insured by the university, "
            "so you do NOT need to apply for SGK insurance through OCW. "
            "METU provides insurance for compulsory summer practices for a period of "
            "20 workdays to 3 months. For voluntary summer practices, insurance is provided "
            "for a period of one month at most, for only one organization. "
            "Insurance is also provided for summer practices conducted abroad."
        ),
    },
    # ── NEW: Systems Design Project (IE 400) ─────────────────────────────
    {
        "id": "ie400-sd-project",
        "topic": "IE 400 Systems Design Project Opportunity",
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
        "page_title": "IE 400 Introduction Slides 2025",
        "content": (
            "During your IE 400 summer practice, you are required to search for a "
            "'Systems Design (SD) Project'. Summer practice is a good opportunity to find "
            "SD projects for your senior year. Look for interesting and challenging problems "
            "at the company and ask engineers about potential challenges. "
            "If you identify a suitable problem, check with the SD committee (not the SP "
            "committee) to verify it is appropriate for a Systems Design project. "
            "Note: The SD project is separate from the IE 400 problem/project requirement."
        ),
    },
    # ── NEW: SP Committee Members (2025-2026) ────────────────────────────
    {
        "id": "committee-members-2025",
        "topic": "SP Committee Members 2025-2026",
        "source_url": "https://sp-ie.metu.edu.tr/en/sp-committee",
        "page_title": "SP Committee",
        "content": (
            "The SP Committee members for the 2025-2026 academic year are: "
            "Prof. Dr. Cem İyigün, Prof. Dr. Esra Karasakal, Çiya Aydoğan, "
            "Buğra Öztürk, Ömer Turan Şahinaslan, Özgür Ünverdi, Mehmet Sencer Zengin. "
            "Contact: ie-staj@metu.edu.tr (this email reaches all committee members). "
            "Before emailing, please check the SP website and meeting slides for answers. "
            "ie-staj@metu.edu.tr is NOT a call center; check existing resources first."
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
            "Fully remote or fully online internships are not accepted for any summer practice. "
            "However, attendance rules vary by case: "
            "IE 300: must be fully face-to-face (manufacturing company only). "
            "IE 400 at a manufacturing company: must be fully face-to-face. "
            "IE 400 at a service company: can be face-to-face OR hybrid (face-to-face + online). "
            "So hybrid is possible only for IE 400 at a service company."
        ),
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
    },
    {
        "question": "Where do I submit my SP report?",
        "answer": (
            "SP reports are collected via ODTUClass in PDF format. "
            "For the 2025-2026 academic year, the due date is October 24, 2025 "
            "(source: IE 300 and IE 400 intro slides 2025-2026). "
            "This is a strict deadline — late submissions are not accepted. "
            "You must register for IE 300 or IE 400 during the registration period of the "
            "Fall semester following your summer practice. "
            "NOTE: For other academic years, check the current intro slides and ODTUClass "
            "for the exact deadline."
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
        "question": "What are the prerequisites for IE 300 and IE 400?",
        "answer": (
            "You can find the full prerequisite chain for all IE courses including "
            "IE 300 and IE 400 at ie.metu.edu.tr/en/prerequisite-chain. "
            "The complete IE curriculum is at ie.metu.edu.tr/en/bs-industrial-engineering-curriculum "
            "(Turkish version: ie.metu.edu.tr/tr/endustri-muhendisligi-lisans-ogretim-programi). "
            "Check these pages to see which courses you need to complete before registering."
        ),
        "source_url": "https://ie.metu.edu.tr/en/prerequisite-chain",
    },
    {
        "question": "Can foreign students do voluntary internships?",
        "answer": (
            "No. Foreign students are NOT allowed to do voluntary internships in Turkey. "
            "A work permit is required for voluntary internships."
        ),
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
    },
    # ── NEW FAQ entries (audit-driven additions) ──────────────────────────
    {
        "question": "Can I do IE 300 in a bank or service company?",
        "answer": (
            "No. IE 300 (Production/Manufacturing Practice) MUST be done at a manufacturing "
            "or production company. Banks, consulting firms, and service-sector companies are "
            "NOT eligible for IE 300. If you want to intern at a bank or service company, "
            "that would count toward IE 400 (Systems/Management/Service Practice) only."
        ),
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
    },
    {
        "question": "Can IE 400 internship be hybrid or partially remote?",
        "answer": (
            "It depends on the company type. "
            "IE 400 at a manufacturing company: NO — must be fully face-to-face at the plant. "
            "IE 400 at a service company: YES — can be face-to-face or hybrid (face-to-face + online). "
            "Fully remote/online is never accepted for any summer practice. "
            "So hybrid is an option for IE 400, but only if your company is a service company."
        ),
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
    },
    {
        "question": "What are the exact prerequisite courses for IE 300?",
        "answer": (
            "To register for IE 300, you must have completed ALL of these: "
            "OHS 101, IE 102, IE 241, IE 251, IE 265, plus at least one of IE 252 or IE 266. "
            "IE 300 is typically taken in the 5th semester (3rd year). "
            "Check the full prerequisite chain at ie.metu.edu.tr/en/prerequisite-chain"
        ),
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
    },
    {
        "question": "What are the exact prerequisite courses for IE 400?",
        "answer": (
            "To register for IE 400, you must have completed IE 300 plus: IE 252, IE 323, "
            "IE 333, and any TWO of the following: IE 304, IE 324, IE 368, IE 372. "
            "IE 400 is typically taken in the 7th semester (4th year). "
            "Check ie.metu.edu.tr/en/prerequisite-chain for details."
        ),
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
    },
    {
        "question": "How is my IE 300 report graded? What is the scoring breakdown?",
        "answer": (
            "IE 300 report is graded out of 200 points total. Breakdown: "
            "Introductory Features (10 pts), Production System Overview (55 pts), "
            "Production Planning and Control (55 pts), Quality Planning and Control (30 pts), "
            "Style and Organization (10 pts), Conclusion (15 pts), plus additional sections. "
            "You must score at least 50% in each section. Grade 125-160 = Incomplete (revision required), "
            "below 125 = Unsatisfactory (repeat at different company). "
            "Reports are due within the first two weeks of the following academic term."
        ),
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
    },
    {
        "question": "How is my IE 400 report graded?",
        "answer": (
            "IE 400 report has two parts: Questions Section (200 pts) and Problem/Project Section (100 pts). "
            "You must pass BOTH separately. Questions: 125-160 = Incomplete (revision), below 125 = Unsatisfactory "
            "(repeat at different company), must score 50% in each section. "
            "Project: 40-65 = Incomplete (revision), below 40 = Unsatisfactory (repeat). "
            "200-pt breakdown: Introductory Features (10), Macro Aspects (20), Production Overview (35), "
            "PPC (50), Quality (20), MIS (20), Work Study (20), Conclusion (15), Style (10)."
        ),
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
    },
    {
        "question": "Which declaration form (beyanname) do I need?",
        "answer": (
            "There are TWO versions of the declaration form: "
            "(1) 'Beyanname - Sağlık Hizmeti Alan' — for students who WILL receive health services "
            "from the company during their internship. "
            "(2) 'Beyanname - Sağlık Hizmeti Almayan' — for students who will NOT receive health services. "
            "Choose the one that matches your situation, print and sign it, and submit via OCW. "
            "Download both from sp-ie.metu.edu.tr/en"
        ),
        "source_url": "https://sp-ie.metu.edu.tr/en",
    },
    {
        "question": "When is the SP report submission deadline?",
        "answer": (
            "For the 2025-2026 academic year, the report due date for both IE 300 and IE 400 is "
            "October 24, 2025 (source: IE 300 and IE 400 Introductory Session slides 2025-2026). "
            "Reports are due within the first 4 weeks of the Fall semester following your summer practice. "
            "This is a STRICT deadline — late submissions are not accepted. "
            "You must also fill out the online questionnaire by this deadline, otherwise your report "
            "is considered incomplete. "
            "NOTE: This date applies to the 2025-2026 year. For other years, always check the "
            "current introduction slides and ODTUClass for the exact due date."
        ),
        "source_url": "https://sp-ie.metu.edu.tr/en/steps-follow",
    },
    {
        "question": "Do I need to fill out an online questionnaire?",
        "answer": (
            "Yes. You are REQUIRED to fill out the online questionnaire on the SP website "
            "(www.ie.metu.edu.tr/~sp). This must be completed before the report submission deadline. "
            "If you do not fill it out, your report will be considered INCOMPLETE regardless of quality. "
            "A separate questionnaire may also be sent via email at the start of the semester."
        ),
        "source_url": "https://sp-ie.metu.edu.tr/en/steps-follow",
    },
    {
        "question": "Can I do IE 400 at the same company where I did IE 300?",
        "answer": (
            "Yes, you can do IE 400 at the same company where you did IE 300, BUT you must work "
            "in a different department or focus on a different area. IE 300 focuses on "
            "production/manufacturing, while IE 400 focuses on systems, management, or service aspects. "
            "The reports must cover different topics and sections."
        ),
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
    },
    {
        "question": "Do I need a separate application form for each company?",
        "answer": (
            "Yes. You must fill out a separate SP Application Form for each company where you plan "
            "to do your internship. There are different forms for IE 300 and IE 400, and for "
            "Turkish and English versions. Download the correct form from "
            "sp-ie.metu.edu.tr/en"
        ),
        "source_url": "https://sp-ie.metu.edu.tr/en",
    },
    {
        "question": "What is the difference between IE 300 and IE 400?",
        "answer": (
            "IE 300 is the Production/Manufacturing Practice — you must intern at a manufacturing "
            "or production company and your report covers production systems, PPC, quality control. "
            "IE 400 is the Systems/Management/Service Practice — you can intern at either a "
            "manufacturing or service company. IE 400 report covers broader topics: macro aspects, "
            "MIS, work study, and includes a mandatory problem/project section (100 extra points). "
            "IE 300 must be completed before IE 400."
        ),
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
    },
    {
        "question": "How do I apply for SGK insurance through OCW?",
        "answer": (
            "Go to OCW (ocw.metu.edu.tr), log in, and navigate to the SP application section. "
            "Fill out the required form with your internship details (company name, dates, etc.). "
            "Submit at least 10 business days before your start date. "
            "After submission, follow up on e-Devlet to verify your SGK registration was processed. "
            "IMPORTANT: If the company already insures you (e.g., paid internship with SSK), "
            "you do NOT need to apply through OCW."
        ),
        "source_url": "https://sp-ie.metu.edu.tr/en/steps-follow",
    },
    {
        "question": "I made a mistake on my SGK application. How do I fix it?",
        "answer": (
            "If you already submitted the OCW form with incorrect information, you should "
            "email ie-staj@metu.edu.tr immediately with the correct details. "
            "If the application has not yet been forwarded to the Rectorate, it may be corrected. "
            "If it was already processed, you may need to cancel the old one and submit a new application. "
            "Include your student ID, old and new information, and the reason for the change."
        ),
        "source_url": "https://sp-ie.metu.edu.tr/en/steps-follow",
    },
    {
        "question": "What is the İşsizlik Fonu Katkısı (Unemployment Fund Contribution)?",
        "answer": (
            "If you are paid during your SP at a PRIVATE company in Turkey, the company must "
            "pay an Unemployment Fund Contribution (İşsizlik Fonu Katkısı). "
            "You need to: (1) Fill out the Paid SP Form on OCW, (2) Get the company to sign "
            "the İşsizlik Fonu Bilgi Formu, (3) Upload the signed form and bank receipt to OCW. "
            "This does NOT apply to unpaid internships or public institutions."
        ),
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
    },
    {
        "question": "What is a project-based internship for IE 400?",
        "answer": (
            "A project-based internship is an alternative format for IE 400 where you work on "
            "a specific industrial engineering problem/project at the company for at least 6 weeks "
            "(30 workdays), instead of the standard 4 weeks. "
            "You must submit a project proposal to the SP Committee BEFORE starting. "
            "If approved, you follow the project-type report format. "
            "The project section is graded separately (100 points) in addition to the regular questions (200 points)."
        ),
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
    },
    {
        "question": "What documents do I need for my summer practice application?",
        "answer": (
            "Required documents vary by situation but typically include: "
            "(1) SP Application Form (from Documents/Forms page), "
            "(2) Declaration Form (Beyanname — choose health service or non-health-service version), "
            "(3) SGK insurance application via OCW (at least 10 days before start), "
            "(4) For paid SP: Paid SP Form, İşsizlik Fonu Bilgi Formu, bank receipt, "
            "(5) Evaluation Form (filled by employer at end of internship, sent to sp-belge@metu.edu.tr). "
            "Download all forms from sp-ie.metu.edu.tr/en"
        ),
        "source_url": "https://sp-ie.metu.edu.tr/en",
    },
    {
        "question": "Can I do a voluntary (gönüllü) internship?",
        "answer": (
            "Yes, Turkish citizens can do voluntary internships in addition to the compulsory "
            "IE 300 and IE 400 summer practices. For voluntary internships, METU provides SGK "
            "insurance for a maximum of one month, for only one organization. "
            "IMPORTANT: Foreign (international) students are NOT allowed to do voluntary "
            "internships in Turkey — a work permit is required. "
            "Apply through OCW using the voluntary internship form."
        ),
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
    },
    {
        "question": "Staj raporumu Türkçe yazabilir miyim?",
        "answer": (
            "Hayır. Staj raporları İngilizce yazılmalıdır. Bu kural hem IE 300 hem de IE 400 "
            "için geçerlidir. Rapor, mürekkeple yazılmalı veya daktilo/bilgisayarla yazılmalıdır. "
            "Detaylar için SP manuallerini inceleyiniz."
        ),
        "source_url": "https://sp-ie.metu.edu.tr/en/general-information",
    },
    {
        "question": "Stajıma kaç gün kaldı ve hâlâ OCW formunu doldurmadım, ne yapmalıyım?",
        "answer": (
            "SGK başvurusu OCW üzerinden staj başlangıcınızdan en az 10 iş günü önce yapılmalıdır. "
            "Eğer bu süreyi kaçırdıysanız, derhal ie-staj@metu.edu.tr adresine mail atarak "
            "durumunuzu açıklayın. Acil durumlarda komite size yardımcı olabilir, ancak "
            "geç başvurularda sigorta başlangıç tarihiniz gecikebilir. "
            "Formunuzu doldurup gönderdikten sonra e-Devlet üzerinden SGK kaydınızı takip edin."
        ),
        "source_url": "https://sp-ie.metu.edu.tr/en/steps-follow",
    },
    {
        "question": "Staj sırasında şirket değiştirmem gerekirse ne yapmalıyım?",
        "answer": (
            "Staj sırasında şirket değiştirmeniz gerekirse, önce ie-staj@metu.edu.tr adresine "
            "mail atarak durumu bildirin. Eski SGK başvurunuzun iptali ve yeni şirket için "
            "yeni SGK başvurusu yapılması gerekecektir. Yeni şirket için ayrı bir SP Application "
            "Form doldurmanız gerekir. Toplam staj sürenizin minimum gereklilikleri karşıladığından "
            "emin olun (IE 300: 20 iş günü, IE 400: 20 veya 30 iş günü)."
        ),
        "source_url": "https://sp-ie.metu.edu.tr/en/steps-follow",
    },
]

import os
import json

_chunks_file = os.path.join(os.path.dirname(__file__), "document_chunks.json")
if os.path.exists(_chunks_file):
    try:
        with open(_chunks_file, "r", encoding="utf-8") as f:
            extra_chunks = json.load(f)
            KNOWLEDGE_CHUNKS.extend(extra_chunks)
    except Exception as e:
        print(f"Error loading document_chunks.json: {e}")
