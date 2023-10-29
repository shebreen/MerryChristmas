const selectTemplateLinks = document.querySelectorAll('.select-template-link');
const resumeEditor = document.getElementById('resume-editor');
const generatedResume = document.getElementById('generated-resume');

selectTemplateLinks.forEach((link) => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        document.getElementById('template-selection').style.display = 'none';
        resumeEditor.style.display = 'block';
    });
});

const resumeForm = document.getElementById('resume-form');
resumeForm.addEventListener('submit', (e) => {
    e.preventDefault();
    generatedResume.style.display = 'block';
    const previewResume = document.getElementById('preview-resume');
    const resumeContent = generateResumeContent();
    previewResume.innerHTML = resumeContent;
});

const downloadButton = document.getElementById('download-resume');
downloadButton.addEventListener('click', () => {
    const resumeContent = generateResumeContent();
    const blob = new Blob([resumeContent], { type: 'application/pdf' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'resume.pdf';
    a.click();
    URL.revokeObjectURL(url);
});
function generateResumeContent() {
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const mobile = document.getElementById('mobile').value;
    const gender = document.getElementById('gender').value;
    const qualification = document.getElementById('qualification').value;
    const college = document.getElementById('college').value;
    const specialization= document.getElementById('specialization').value;
    const gradYear = document.getElementById('gradYear').value;
    const resumeContent = `
    <p>Name: ${name}</p>
    <p>Email: ${email}</p>
    <p>Mobile Number: ${mobile}</p>
    <p>Gender: ${gender}</p>
    <p>Highest Qualification: ${qualification}</p>
    <p>College: ${college}</p>
    <p>Specialization/Branch: ${specialization}</p>
    <p>Year of Graduation: ${gradYear}</p>
    `;
    return resumeContent;
}
