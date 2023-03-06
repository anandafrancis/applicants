import streamlit as st

def page_home():
    st.title('Home')
    st.write('\n')

    st.header('What is Black Excellence?')
    st.write('At the heart of Black Excellence lies three foundational pillars that define us: civic engagement, pursuit of knowledge, and preservation.')
    
    with st.expander("CIvic Engagement"):
        st.write('Civic engagement calls us to serve our community with an unwavering passion, using every opportunity we have been given to create opportunities for others. We believe that individual success is intimately linked to the success of our community as a whole, and we strive to uplift those around us at every turn.')
   
    with st.expander("Pursuit of Knowledge"):
        st.write('Pursuit of knowledge is a relentless journey of exploration that can take many forms. We embrace traditional education pathways, but we also recognize the value of self-teaching, podcasts, online courses, workshops, conferences, programs, and bootcamps. Whether we are learning from work or volunteering, we relentlessly seek to expand our knowledge and hone our skills.')
    
    with st.expander("Preservation"):
        st.write('Preservation is a vital component of Black Excellence, as we understand the importance of taking time to heal our community and ourselves. By focusing on our emotional and physical wellness, and by addressing harmful attributes within our communities, we are able to heal one another and create a brighter future for all. We know that by working together, we can preserve our community and ensure that it thrives for generations to come.')

    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.header('What is our “Pipeline”?')
    st.write('At Black Excellence Pipeline, our community network is built by fostering connections based on shared ethnic backgrounds, hobbies, personal projects, career goals, shared experiences, and mentorship. Our pipeline provides a platform for individuals to network and support each other as they strive for excellence."')

    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.header('How can you get involved?')
    st.write('here are many ways to get involved at BEP. Below we have outlined the different ways to be involved.')
    
    with st.expander("Board of Directors"):
        st.write('The Board of Directors is a group of individuals who are responsible for overseeing the management and direction of the nonprofit organization. They provide strategic guidance, make decisions on behalf of the organization, and ensure that BEP is meeting its mission and long-term goals of making a positive impact on the Black community. ')

    with st.expander("Staff"):
        st.write("There are 5 different departments BEP staff can work in. In the Software Development department, staff members use their technical expertise to develop and maintain the organization's digital platforms and tools. The Branding department is responsible for creating and maintaining the BEP brand, ensuring that the organization's message is clear and consistent across all platforms. The Research department conducts studies and collects data to better understand the needs of the Black community and inform BEP's strategies and initiatives to our corporate sponsors and university partners. The Fundraising department works towards securing financial support and resources for the organization's programs and initiatives. The Programs team is responsible for creating and managing the programs and services that BEP provides to the community, while the Events team plans and executes the organization's events. For more information about each department navigate the sidebar on the left which will")

    with st.expander("Freelancers"):
        st.write("Freelancers are project-based staff members. We recognize that everyone's time and availability may vary due to different commitments such as school, work, and personal obligations. Therefore, we offer the opportunity for individuals to contribute to specific projects that align with their interests and availability. You  have the flexibility to work on different teams and engage in various roles, contributing to our mission in a meaningful way. To learn more about this opportunity, visit our Freelancer page for further information.")

    with st.expander("Campus Ambassadors"):
        st.write("Campus Ambassadors play a critical role in spreading the word about Black Excellence Pipeline and its mission on college campuses. They serve as a liaison between their respective campuses and the organization, promoting our programs and events to students, faculty, and staff. They help increase visibility and awareness of our organization within their communities, participate in recruitment efforts for our various teams, and help coordinate events and activities. To learn more about this opportunity, visit our Campus Ambassadors page for further information.")

    with st.expander("BEP Membership"):
        st.write("BEP Members are more than just names on a list. To us, they are a community of individuals who share a common goal: to uplift and support one another in the pursuit of excellence. As such, we welcome anyone who identifies as Black (across the diaspora) and is committed to civic engagement, preservation, and the pursuit of knowledge. More information about benefits and the application process can be found on our “BEP Membership” page.")

    with st.expander("Corporate Sponsors"):
        st.write("Corporate Sponsors can not only support the development of a diverse and talented workforce but also contribute to the growth of their brand by demonstrating their commitment to diversity, equity, and inclusion. Support can come in various ways including funding events and programs, sponsoring scholarships and fellowships, offering internships and job opportunities, and providing mentorship and professional development opportunities to our members. In return, we offer corporate sponsors access to our talented and diverse community, opportunities to network and build relationships. Join us in creating a more equitable and inclusive future by becoming a corporate sponsor of Black Excellence Pipeline. To learn more about this opportunity, visit our Corporate Sponsors page for further information.")

    with st.expander("Community Partners"):
        st.write("Community Partners gain access to our network of talented and driven individuals, and can participate in events and initiatives that promote community building, civic engagement and personal growth. We work closely with our partners to develop mutually beneficial programs and collaborations that align with our mission of promoting Black excellence. To learn more about this opportunity, visit our Community Partners page for further information.")

    with st.expander("Donors"):
        st.write("Donors are valued by our organization as we rely on the generosity of donors to support our programs and initiatives. By making a donation to our organization, you can help us empower and uplift Black individuals by providing opportunities for community building, professional development, and mentorship. Donors can choose to support our general fund, which allows us to allocate resources where they are needed most, or they can choose to donate specifically to one of our programs or initiatives. By donating to Black Excellence Pipeline, you can play a vital role in creating a more equitable and inclusive future. To learn more about this opportunity, visit our Donors page for further information.")

    with st.expander("Supporters"):
        st.write("Supporters can show love by subscribing to our newsletters, following our social media accounts, or offering advice and resources that could help us in our development, your contributions help to sustain and grow our organization. As we strive to create a community dedicated to uplifting and supporting one another, we welcome all forms of support and are grateful for those who choose to stand with us on this journey.")


def timeline():
    st.title("Timeline")
    st.write("We are working towards creating a timeline for our different projects to give you a better understanding of our deadlines and where you may see yourself stepping in and helping us do this great work.")

def board_page():
    st.title("Board of Directors Job Posting")
    st.write('\n')
    st.write('\n')
    
    responsibilities = ["Attend board meetings on a regular basis and actively participate in discussions and decision-making processes.", 
                        "Provide guidance and support to the organization's leadership team.",
                        "Monitor and evaluate the organization's performance, programs, and operations.",
                        "Work with the team to develop and implement strategic plans.",
                        "Help identify and cultivate relationships with potential donors, sponsors, and partners.",
                        "Represent the organization in various events and activities.",
                        "Help recruit and onboard new board members and staff."
                        ]
    
    quals = ["Passion for the organization's mission and a strong commitment to social impact.",
             "Previous experience in a leadership or board member role.", 
             "Excellent communication, interpersonal, and problem-solving skills.",
             "Knowledge of nonprofit governance, operations, and best practices.", 
             "Ability to work collaboratively with others and build consensus.",
             "Experience in fundraising, grant writing, or donor relations is a plus."]
    
    st.write("We are currently seeking a highly motivated and skilled individual to join our Board of Directors at our student led nonprofit organization. As a Board of Director, you will work closely with other board members to provide oversight and strategic direction for the organization. Your role will be crucial in helping us achieve our mission and goals.")
    st.write('\n')
    
    st.subheader("Responsibilities")
    for item in responsibilities:
        st.write("- " + item)

    st.write('\n')
    st.write('\n')
    st.subheader("Qualifications")
    for item in quals:
        st.write("- " + item)

    st.write('\n')
    st.write('\n')
    st.write('We offer a flexible and dynamic work environment that is dedicated to supporting and developing our team members. If you are looking for an opportunity to make a meaningful impact in your community and gain valuable leadership experience, we encourage you to apply for this position. This position is fully remote and unpaid.')

def swe_page():
    st.title('Software Development Team')
    st.write('\n')
    st.write('\n')

    st.header("The Cookout: BEP's Social Media Platform")
    st.write('\n')
    st.write('\n')

    st.write("Black Excellence Pipeline was born out of a desire to provide a much-needed sense of community during difficult times in the pandemic. Unfortunately, we found that over time we struggled to maintain consistent communication with our stakeholders, and our events often fall short of making a significant impact. That's why we propose to create sub-communities within the black collegiate space through an app, offering local, school-based, hobby-based, professional, social and cultural groups. By using user data, we can allocate funding and plan events based on specific needs and preferences of active subcommunities, creating a direct pipeline of community, discussion, and opportunity.")
    st.write('\n')
    st.write('\n')

    st.write("What sets our platform apart is its ability to automatically add users to communities based on their interests, using data from other platforms and the data the user produces on the app. This means that users don't need to search for these communities; the community finds them. Our platform will serve as a research and data collection tool for our users/stakeholders and a source of information for funding and event planning.")
    st.write('\n')
    st.write('\n')
    
    st.write("Our team plans to develop a website proof of concept to confirm the features and user experience we want to achieve. We will then create a website and mobile application prototype, first on iOS, then on Android, to showcase to potential investors and sponsors. Once we have secured enough funding to develop a minimum viable product, we plan to release refined test versions within Boston and DC campuses. We are looking for passionate developers to join our team and help us bring this innovative and impactful idea to life.")

def research_page():
    st.title('Research Team')
    st.write('\n')
    st.write('\n')

    st.subheader('The Color Line: Examining Barriers to Success for Black Individuals in Education and Industry')
    st.write('\n')
    st.write('\n')

    st.write("Our proposed initiative seeks to address the critical issue of low Black matriculation rates in higher education institutions and underrepresentation in different industries. By partnering with prestigious universities as well as corporations, we can pool resources and expertise to gather data and conduct research on the root causes of this issue. Our goal is to identify and address systemic racism and inequality in education and job acquisition and lack of resources and support for Black students, applicants and employees")
    st.write('\n')
    st.write("Through our research, we aim to develop innovative policy solutions to increase Black matriculation rates in higher education and DEI initiatives to improve Black presence in current underrepresented industries. This includes advocating for increased funding and resources for historically black colleges and universities, supporting initiatives to improve access to financial aid and scholarships for black students, creating corporate partnerships with organizations like our own to increase Black applicants presence during the interview process and creating mentorship and support programs for Black students and professionals.")
    st.write('\n')
    st.write("Our approach is unique in that we plan to leverage the power of technology to generate data and engage directly with students. We will develop an app that not only collects data but also invites students to participate in our research.")
    st.write('\n')
    st.write("We believe that our initiative has the potential to grow into a think tank that addresses a range of issues related to racial inequality and social justice in education and industry. We encourage student researchers to join our team in this important work. By working together, we can create a brighter future for Black students and applicants and promote equity and justice in education and industry for all.")


def events_page():
    pass

def programs_page():
    pass

def fund_page():
    pass

def membership_page():

    benefits = [
        "​​Providing access to exclusive resources and materials",
        "Offering training and professional development opportunities", 
        "Creating a community of like-minded individuals for networking and collaboration", 
        "Providing mentoring and coaching programs",
        "Hosting events and conferences for networking and learning",
        "Offering discounts or special offers to members",
        "Providing opportunities to volunteer and give back to the community",
        "Advocating for change and influencing policy decisions",
        "Offering scholarships and grants for education or career advancement",
        "Hosting webinars and online training sessions",
        "Providing access to specialized equipment or technology",
        "Offering free or discounted access to educational resources, such as books or journals",
        "Creating a referral network to help members find employment or business opportunities",
        "Offering financial planning and assistance programs",
        "Providing support and counseling services, such as mental health or addiction services",
        "Offering legal and accounting services",
        "Providing resources for personal and professional development, such as leadership training or time management resources",
        "Hosting social events and gatherings to build community and camaraderie",
        "Offering health and wellness programs, such as exercise classes or nutrition workshops",
        "Providing access to opportunities for community service and activism"

    ]
    
    st.title("BEP Membership")
    st.write('\n')
    st.write('\n')

    st.header("Benefits")
    st.write('\n')
    st.write("At BEP we strive to add value to our members. Here is a list of various initiatives being worked on by our team to ensure members have the best chance and accessibility of resources for success!")
    st.write('\n')
    for item in benefits:
        st.write("- " + item)


    st.header("Membership Application")
    st.write('\n')
    st.write('\n')
    st.write("Our application process is straightforward yet meaningful. In addition to the typical fill-in-the-blanks, we require a personal statement. This statement is your opportunity to share your unique story with us, and to tell us why you want to be a BEP member. We want to hear how you plan to embody our three pillars: civic engagement, preservation, and knowledge.")
    st.write("Joining BEP means becoming part of a community that is invested in your success. We want to support you as you pursue your dreams, and we believe that together, we can make a positive impact in our communities and beyond.")
def main():

    # Create dictionary with page names as keys and corresponding functions as values
    pages = {
        "Home": page_home,
        "Timeline": timeline,
        "Board of Directors": board_page,
        "Software Development Team": swe_page,
        "Research Team": research_page,
        "BEP Membership": membership_page
    }

    # Display pages as tabs in the sidebar
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(pages.keys()))
    page = pages[selection]
    page()
   
    

if __name__ == '__main__':
    main()