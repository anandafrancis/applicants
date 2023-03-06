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

def page_contact():
    st.title("Contact")
    st.write("Contact us here.")


def main():

    # Create dictionary with page names as keys and corresponding functions as values
    pages = {
        "Home": page_home,
        "Timeline": timeline,
        #"Contact": page_contact
    }

    # Display pages as tabs in the sidebar
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(pages.keys()))
    page = pages[selection]
    page()
   
    

if __name__ == '__main__':
    main()