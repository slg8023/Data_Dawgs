import pandas as pd

# Load the dataset
# Replace 'your_file_name.csv' with the actual name of your file
file_path = 'rawAweExperienceSurveyResponses.csv'
df = pd.read_csv(file_path)

# Display the first 5 rows to confirm it loaded correctly
print("--- Initial Data Preview ---")
print(df.head())

# Check the column names to ensure they match our expectations
# print("\n--- Column Names ---")
# print(df.columns.tolist())
# 68 columns

# ----------

# Make a copy of the df
cleaned_df = df.copy()
# print(cleaned_df.head())

# ----------

# Renaming the columns with short-form names, 
# using dict becuse it doesn’t matter if column order changes later, 
# the code will only rename the matches it finds

# The mapping dictionary (Original Name: New Name)
column_mapping = {
    'Timestamp': 'timestamp',
    'Please select your age range': 'age_range',
    'Which best describes the environment you spent the most time growing up in?': 'env_growth',
    'How would you describe your worldview or spiritual orientation?': 'worldview',
    'Which category best describes your primary daily activity? ': 'activity_primary',
    'Do you regularly engage in any of the following practices?': 'regular_practices',
    'Including yourself, how many people live in your household?': 'household_size',
    'What is your assigned gender at birth? ': 'gender_assigned',
    'What is your current gender identity? ': 'gender_identity',
    'What is your highest completed degree?': 'edu_level',
    'What is your current income bracket?': 'income_bracket',
    'What describes your socioeconomic status growing up? ': 'socioec_status',
    'What college do you attend?': 'college_name',
    'I regularly notice beauty around me.': 'awe_scale_1',
    'I stay open to someone’s opinion even when it differs from mine.': 'awe_scale_2',
    'I have a lot of intellectual curiosity. ': 'awe_scale_3',
    'I am drawn to experiences, ideas, and sensations that are unfamiliar or challenge my current way of seeing the world.': 'awe_scale_4',
    'I prefer routine and spending time with people who think similarly to myself.': 'awe_scale_5',
    'Do people ever describe you as lost in thought?': 'awe_scale_6',
    'I can become deeply absorbed in nature, music, art, beliefs, or ideas.': 'awe_scale_7',
    'I sometimes become so involved in a piece of music or art that I lose all sense of time and my surroundings.': 'awe_scale_8',
    'I tend to have intense or vivid dreams.': 'awe_scale_9',
    'My dreams tend to be more associated with nightmares or stress.': 'awe_scale_10',
    'I can remember my dreams when I wake up in the morning.': 'awe_scale_11',
    'I do not become absorbed in stimuli or surroundings.': 'awe_scale_12',
    'To confirm you are paying attention, please select number 3 for this question. ': 'control',
    'Have you ever been moved in a way that evokes strong emotional memories?': 'trigger_moved_1',
    'Have you ever been moved to tears, emotionally touched, stirred or experienced something that warmed your heart?': 'trigger_moved_2',
    'Do you experience moments that make you feel deeply connected with nature?': 'trigger_moved_3',
    'Do you experience moments that make you feel deeply connected with the people around you?': 'trigger_moved_4',
    'I do not feel deep connections to the world or people around me.': 'trigger_moved_5',
    'I enjoy volunteering or serving others in my community.': 'trigger_moved_6',
    'I am easily and often moved by the beauty, humor, and goodness I encounter in everyday life.': 'trigger_moved_7',
    'I do not often feel joy, contentment, amusement, compassion, and pride.': 'trigger_moved_8',
    'I feel part of a much larger whole.': 'trigger_moved_9',
    'I do not often experience powerful feelings connected to the greater world around me.': 'trigger_moved_10',
    'I notice physical sensations in my body when I experience emotions (e.g., tension, breathing/heart rate changes, etc.)': 'trigger_phys_1',
    'Even when I feel intense physical sensations, I feel that my body is in a safe and trustworthy place.': 'trigger_phys_2',
    'I listen to my body for information to help me understand how I am truly feeling about a situation.': 'trigger_phys_3',
    'I notice how my breathing becomes free and easy when I feel comfortable.': 'trigger_phys_4',
    'My emotions do not trigger physical responses.': 'trigger_phys_5',
    'I take stock in my thoughts and emotions without getting overwhelmed by them.': 'trigger_phys_6',
    'I am aware of my body sensations and breathing in response to situations and things happening around me.': 'trigger_phys_7',
    'When stressed, I focus on calming or seek awe experiences for relief.': 'trigger_phys_8',
    'I listen to my body during stressful or triggering situations before responding.': 'trigger_phys_9',
    'I believe in trusting my hunches.': 'trigger_interpersonal_1',
    'How frequently do you experience Deja Vu? ': 'trigger_interpersonal_2',
    'I prefer concrete facts over abstract theories.': 'trigger_interpersonal_3',
    'I have had the experience of suddenly knowing something to be true without being able to explain how I gained that information. ': 'trigger_interpersonal_4',
    'I tend to notice coincidence or synchronicities often. ': 'trigger_interpersonal_5',
    'When I meditate, pray, or engage in spiritual or religious practices, I feel deeply connected to something or someone greater than myself.': 'trigger_spiritual_1',
    'I believe life has a deeper meaning or purpose.': 'trigger_spiritual_2',
    'I consider myself highly engaged with routine spiritual practices.': 'trigger_spiritual_3',
    'I do not consider myself religious or spiritual.': 'trigger_spiritual_4',
    'I see myself as resilient and able to handle challenges.': 'trigger_interpersonal_6',
    'When things go wrong, it’s usually someone else’s fault.': 'trigger_interpersonal_7',
    'Challenges cause me to feel overwhelmed and stuck.': 'trigger_interpersonal_8',
    'How strongly do you believe in meaningful coincidences?': 'trigger_interpersonal_9',
    'Do you believe in universal energy such as chakras, kundalini, etc?': 'trigger_spiritual_5',
    'How strongly do you believe in a God or divine being?': 'trigger_spiritual_6',
    'Do you believe in souls, spirits, or unseen beings?': 'trigger_spiritual_7',
    'How strongly do you believe in karma or moral causation? ': 'trigger_spiritual_8',
    'During powerful experiences, my awareness of myself fades into the background.': 'trigger_phys_10',
    'During powerful moments, I have the physical sensation that my body is shrinking or becoming very small in relation to the world around me.': 'trigger_phys_11',
    'During powerful moments, I feel that time is slowing down or speeding up.': 'trigger_phys_12',
    'Emotional or inspiring experiences give me chills or goosebumps.': 'trigger_phys_13',
    'I can give myself chills or goosebumps with no external stimuli (such as music, cold temperature, or emotional videos).': 'chills_ability',
    'How often are you able to produce chills without external stimuli?': 'chills_freq',
}

# Apply the rename
cleaned_df.rename(columns=column_mapping, inplace=True)

# Verify the change
# print(cleaned_df.shape)
# (107, 68)

# ----------

# Filtering: Drop any responses where control == 3

cleaned_df = cleaned_df[cleaned_df['control'] == 3]

# Reset the index so the row numbers are sequential again
cleaned_df.reset_index(drop=True, inplace=True)
# print(cleaned_df.shape)
# (101, 68)

# ----------

# Convert string scale values to integers

# 1. Conversion of ordinal belief columns to numeric values
belief_mapping = {
    'Not at all': 1,
    'Slight belief': 2,
    'Moderate belief': 3,
    'Strong belief': 4,
    'Very strong belief': 5
}

belief_columns = [
    'trigger_interpersonal_9',
    'trigger_spiritual_5',
    'trigger_spiritual_6',
    'trigger_spiritual_7',
    'trigger_spiritual_8'
]

for col in belief_columns:
    cleaned_df[col] = cleaned_df[col].map(belief_mapping)

# print(cleaned_df[belief_columns].head())

# 2. Conversion of chills_ability to binary
# 0 = No and Not Sure, 1 = Yes
chills_mapping = {
    'No': 0,
    'Not Sure': 0,
    'Yes': 1
}

cleaned_df['chills_ability'] = cleaned_df['chills_ability'].map(chills_mapping)

# print(cleaned_df[['chills_ability']].head())

# 3. Conversion of chills_freq to ordinal numeric values
# 1 = Never - 5 = Very Often
chills_freq_mapping = {
    'Never': 1,
    'Rarely': 2,
    'Sometimes': 3,
    'Often': 4,
    'Very Often': 5
}

cleaned_df['chills_freq'] = cleaned_df['chills_freq'].map(chills_freq_mapping)

# print(cleaned_df[['chills_freq']].head())

# 4. Convert all float64 columns to nullable Int64
float_cols = cleaned_df.select_dtypes(include=['float64']).columns
for col in float_cols:
    cleaned_df[col] = cleaned_df[col].astype('Int64')

# pd.set_option('display.max_rows', None)
# print(cleaned_df.dtypes)

# ----------

# Clean demographic columns

# 1. Consolidate household_size: 1 and 2 -> "<=2"
cleaned_df['household_size'] = cleaned_df['household_size'].replace(['1', '2'], '<=2')

# print(cleaned_df['household_size'].unique())   
# print(cleaned_df[['household_size']].head())

# 2. Clean edu_level
cleaned_df['edu_level'] = cleaned_df['edu_level'].replace({
    'AA': 'Associates Degree',
    'High school Diploma': 'High school Diploma/GED',
    'GED': 'High school Diploma/GED'
})

# 3. Clean college_name
college_mapping = {
    'Seattle unversity': 'Seattle University',
    'Seattle central': 'Seattle Central College',
    'UOregon': 'University of Oregon',
    'Washington state University': 'Washington State University',
    'wcc': 'Whatcom Community College'
}
cleaned_df['college_name'] = cleaned_df['college_name'].replace(college_mapping)

# ----------

# Add net new columns

# 1. Binary UW vs Other column
cleaned_df['is_uw_student'] = (cleaned_df['college_name'] == 'University of Washington').astype(int)

# print(cleaned_df.shape)
# (101, 69)

# 2. Categorize colleges by Region and Type
def categorize_college(name):
    name = str(name).strip()
    if name == 'University of Washington' or name == 'Washington State University':
        return 'WA State Public'
    if name == 'Seattle University':
        return 'WA State Private'
    if name in ['Seattle Central College', 'South Seattle College', 'Whatcom Community College']:
        return 'Community College'
    if name in ['University of Oregon', 'University of Minnesota', 'The College of William and Mary', 'Ohio State University']:
        return 'Out-of-State Public'
    if name in ['Pomona College', 'Yeshiva University', 'University of Chicago', 'Dartmouth College', 'University of Southern California']:
        return 'Out-of-State Private'
    if name == 'Sharif University of Technology (Tehran, Iran)':
        return 'International'
    return 'Other/Multiple'

cleaned_df['college_type'] = cleaned_df['college_name'].apply(categorize_college)

# print(cleaned_df.shape)
# (101, 70)


# ----------

# Export the cleaned data to a new CSV file
print("--- Final Cleaned Data Preview ---")
print(cleaned_df.head())

output_file = 'cleanedAweExperienceSurveyResponses.csv'
cleaned_df.to_csv(output_file, index=False)

print(f"\n--- Export Complete ---")
print(f"Cleaned data saved to: {output_file}")

