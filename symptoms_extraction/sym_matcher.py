import difflib
import rake_nltk

# Patient's problem sentence

# Symptoms list
columns = "itching,skin_rash,nodal_skin_eruptions,continuous_sneezing,shivering,chills,joint_pain,stomach_pain,acidity,ulcers_on_tongue,muscle_wasting,vomiting,burning_micturition,spotting_ urination,fatigue,weight_gain,anxiety,cold_hands_and_feets,mood_swings,weight_loss,restlessness,lethargy,patches_in_throat,irregular_sugar_level,cough,high_fever,sunken_eyes,breathlessness,sweating,dehydration,indigestion,headache,yellowish_skin,dark_urine,nausea,loss_of_appetite,pain_behind_the_eyes,back_pain,constipation,abdominal_pain,diarrhoea,mild_fever,yellow_urine,yellowing_of_eyes,acute_liver_failure,fluid_overload,swelling_of_stomach,swelled_lymph_nodes,malaise,blurred_and_distorted_vision,phlegm,throat_irritation,redness_of_eyes,sinus_pressure,runny_nose,congestion,chest_pain,weakness_in_limbs,fast_heart_rate,pain_during_bowel_movements,pain_in_anal_region,bloody_stool,irritation_in_anus,neck_pain,dizziness,cramps,bruising,obesity,swollen_legs,swollen_blood_vessels,puffy_face_and_eyes,enlarged_thyroid,brittle_nails,swollen_extremeties,excessive_hunger,extra_marital_contacts,drying_and_tingling_lips,slurred_speech,knee_pain,hip_joint_pain,muscle_weakness,stiff_neck,swelling_joints,movement_stiffness,spinning_movements,loss_of_balance,unsteadiness,weakness_of_one_body_side,loss_of_smell,bladder_discomfort,foul_smell_of urine,continuous_feel_of_urine,passage_of_gases,internal_itching,toxic_look_(typhos),depression,irritability,muscle_pain,altered_sensorium,red_spots_over_body,belly_pain,abnormal_menstruation,dischromic _patches,watering_from_eyes,increased_appetite,polyuria,family_history,mucoid_sputum,rusty_sputum,lack_of_concentration,visual_disturbances,receiving_blood_transfusion,receiving_unsterile_injections,coma,stomach_bleeding,distention_of_abdomen,history_of_alcohol_consumption,fluid_overload,blood_in_sputum,prominent_veins_on_calf,palpitations,painful_walking,pus_filled_pimples,blackheads,scurring,skin_peeling,silver_like_dusting,small_dents_in_nails,inflammatory_nails,blister,red_sore_around_nose,yellow_crust_ooze"
symptoms_list = columns.split(',')

# Function to find similar symptoms in the sentence
def extract_keywords(text):
  """Extracts keywords from a text using the rake_nltk library."""
  r = rake_nltk.Rake()
  r.extract_keywords_from_text(text)
  keywords = r.get_ranked_phrases()
  act_keys = []
  for i in keywords:
    temp = i.split()
    for j in range(len(temp)):
      if temp[j] == "pain" or temp[j] == "skin":
        act_keys.append(temp[j-1] + " " + temp[j])
        try:
          act_keys.append(temp[j] + " " + temp[j+1])
        except:
          pass
      else:
        act_keys.append(temp[j])
  return act_keys

def match_symptoms(keywords, symptoms):
  """Matches keywords to symptoms using the difflib library."""
  matches = []
  for keyword in keywords:
    for symptom in symptoms:
      if difflib.SequenceMatcher(None, keyword, symptom).ratio() > 0.6:
        matches.append((symptom))
  return matches

# Example usage:

text = " I have fever throat pain. I have cold and cough I have headache for post two days"

# Extract keywords from the text.
keywords = extract_keywords(text)

# Match keywords to symptoms.
matches = match_symptoms(keywords, symptoms_list)

# Print the matches.
print(matches)