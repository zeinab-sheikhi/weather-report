from models.cfg_rule import CFGRule

toy_rules = [
    CFGRule(lhs="S", rhs=["AFFIRMATION", "."]),
    CFGRule(lhs="S", rhs=["INTERROGATIVE", "?"]),
    
    CFGRule(lhs="AFFIRMATION", rhs=["NP-3-S", "VP-3-S"]),      # declarative sentence for 3rd singular
    CFGRule(lhs="AFFIRMATION", rhs=["NP-3-S", "VP-Rel-3-S"]),  # declarative sentence for 3rd singular with a relative clause
    
    CFGRule(lhs="INTERROGATIVE", rhs=["AUX-3-S", "NP-3-S", "VP-N-3-S"]),      # interrogative sentence for 3rd singular
    CFGRule(lhs="INTERROGATIVE", rhs=["AUX-3-S", "NP-3-S", "VP-Rel-N-3-S"]),  # interrogative sentence for non 3rd singular
    CFGRule(lhs="INTERROGATIVE", rhs=["AUX-Past", "NP-3-S", "Vi"]),           # interrogative sentence for past
    
    CFGRule(lhs="VP-Rel-N-3-S", rhs=["Vi-Rel-Clause", "Rel-Clause"]),     # VP with a relative clause for non 3rd singular verbs
    CFGRule(lhs="VP-Rel-3-S", rhs=["V-Rel-Clause-3-S", "Rel-Clause"]),    # VP with a relative clause for 3rd singular verbs
    CFGRule(lhs="VP-Rel-past", rhs=["V-Rel-Clause-Past", "Rel-Clause"]),  # VP with a relative clause for past verbs 
    
    CFGRule(lhs="Rel-Clause", rhs=["Rel-Pronoun", "AFFIRMATION"]),  # relative clause 

    CFGRule(lhs="NP-3-S", rhs=["Proper-Noun"]),  # NP for 3rd singular nouns
    CFGRule(lhs="Proper-Noun", rhs=["Sabine"]),  # proper noun
    CFGRule(lhs="Proper-Noun", rhs=["Jamy"]),
    CFGRule(lhs="Proper-Noun", rhs=["Fred"]),    
     
    CFGRule(lhs="VP-N-3-S", rhs=["Vi"]),  # VP for non 3rd singular 
    CFGRule(lhs="VP-N-3-S", rhs=["Vi", "NP-3-S"]), 
        
    CFGRule(lhs="VP-3-S", rhs=["V-3-S"]),  # VP for 3rd singular 
    CFGRule(lhs="VP-3-S", rhs=["V-3-S", "NP-3-S"]), 

    CFGRule(lhs="Vi", rhs=["hear"]),      # bare infinitive verb
    CFGRule(lhs="V-3-S", rhs=["hears"]),  # 3rd singular form of a verb
    CFGRule(lhs="V-3-S", rhs=["reads"]), 
    CFGRule(lhs="V-3-S", rhs=["writes"]), 
    
    CFGRule(lhs="Vi-Rel-Clause", rhs=["believe"]),  # bare infinitive verbs that are followed by a relative clause
    CFGRule(lhs="Vi-Rel-Clause", rhs=["say"]), 
    CFGRule(lhs="Vi-Rel-Clause", rhs=["think"]), 
    CFGRule(lhs="V-Rel-Clause-3-S", rhs=["believes"]),  # 3rd singular form of verbs that are followed by a relative clause
    CFGRule(lhs="V-Rel-Clause-3-S", rhs=["says"]), 
    CFGRule(lhs="V-Rel-Clause-3-S", rhs=["thinks"]), 
    CFGRule(lhs="V-Rel-Clause-Past", rhs=["said"]),  # past form of verbs that are followed by a relative clause
    
    CFGRule(lhs="AUX", rhs=["Do"]),        # auxiliary bare inifinitive verb
    CFGRule(lhs="AUX-3-S", rhs=["Does"]),  # auxiliary 3rd singular verb 
    CFGRule(lhs="AUX-Past", rhs=["Did"]),  # auxiliary past verb

    CFGRule(lhs="Rel-Pronoun", rhs=["that"])  # Relative Pronoun
]

weather_rules = [
    CFGRule(lhs="FORECAST", rhs=["HEADLINE", ".", "S", "S", "S", "S", "S", "S", "S", "S", "S"]),
    CFGRule(lhs="HEADLINE", rhs=["Weather Forecast", "NOM-TIME-PP"]),
    CFGRule(lhs="S", rhs=["DECLARATIVE", "."]),
    CFGRule(lhs="S", rhs=["DECLARATIVE", "CONJ-BUT", "DECLARATIVE", "."]),  # DECLARATIVE ---> DECLARATIVE but DECLARATIVE
    
    CFGRule(lhs="DECLARATIVE", rhs=["NP-3-S", "VP-3-S"]),  # NP VP for 3rd singular (S ---> NP VP)
    CFGRule(lhs="DECLARATIVE", rhs=["NOM-3-S", "VP-P-3-S"]),  # 3rd singular nominal followed by a passive verb (S ---> Nominal VP)
    CFGRule(lhs="DECLARATIVE", rhs=["NOM-N-3-S", "VP-P-N-3-S"]),  # non 3rd singular nominal followed by a passive verb (S ---> Nominal VP)
    CFGRule(lhs="DECLARATIVE", rhs=["NOM-N-3-S", "VP-P-N-3-S", "RANGE"]), 
    CFGRule(lhs="DECLARATIVE", rhs=["NOM-GERUND", "DIR-PP"]),  # nominal gerund followed by direction persposition phrase (Nominal ---> NominalGerund PP)
    CFGRule(lhs="DECLARATIVE", rhs=["TIME-PP", ",", "NOM-3-S", "VP-P-3-S"]),    # (S ---> PP Nominal VP)
    CFGRule(lhs="DECLARATIVE", rhs=["NOM-3-S", "VP-P-3-S", "PP"]),              # (S ---> PP Nominal VP PP)
    CFGRule(lhs="DECLARATIVE", rhs=["TIME-PP", ",", "NOM-3-S", "VP-P-3-S", "PP"]), 
    
    CFGRule(lhs="NP-3-S", rhs=["DT-NN-WEATHER"]),               # NP for 3rd singular nouns (NP ---> Det Noun)
    CFGRule(lhs="NOM-3-S", rhs=["JJ-NP"]),                      # nominal 3rd singular (Nominal ---> adjective Noun)
    CFGRule(lhs="NOM-N-3-S", rhs=["QNT-NP-P"]),                 # nominal non 3rd singular (Nominal ---> quantifier Noun)
    CFGRule(lhs="NOM-GERUND", rhs=["NN-WIND", "GERUND-WIND"]),  # nominal gerund (Nominal ---> Nominal Gerund)

    CFGRule(lhs="PROP-NN", rhs=["CITY"]),  # proper noun
    
    CFGRule(lhs="DT-NN", rhs=["DT", "NN"]),  # determiner followed by a noun (NP ---> Det Noun)
    CFGRule(lhs="DT-NN", rhs=["DT", "NNS"]),
    CFGRule(lhs="DT-NN-WEATHER", rhs=["DT", "NN-WEATHER"]),  # determiner followed by weather as the noun
    CFGRule(lhs="DT-NN-TIME", rhs=["DT", "PART-OF-DAY-NN"]),  # determiner followed by time
    
    CFGRule(lhs="JJ-NP", rhs=["JJ", "NN"]),                  # Nominal ---> adjective Noun
    CFGRule(lhs="JJ-NP", rhs=["JJ-WEATHER", "NN-WEATHER"]),  # specific adjective with the weather Noun
    CFGRule(lhs="TIME-JJ-NN", rhs=["TIME-JJ", "WEEK-DAYS"]), 

    CFGRule(lhs="QNT-NP-P", rhs=["QNT-P", "NNS"]),  # noun phrase with pural quantifer

    CFGRule(lhs="VP-3-S", rhs=["V-3-S", "JJ"]),            # VP ---> Verb NP
    CFGRule(lhs="VP-3-S", rhs=["VP-MODAL", "ADJP"]),       # VP ---> Verb AP
    CFGRule(lhs="VP-P-3-S", rhs=["V-3-S", "V-PAST"]),      # VP passive for 3rd singular
    CFGRule(lhs="VP-P-N-3-S", rhs=["V-N-3-S", "V-PAST"]),  # VP Passive for non 3rd singular
    CFGRule(lhs="VP-MODAL", rhs=["V-MODAL", "Vi"]),        # VP with modal verb
    
    CFGRule(lhs="Vi", rhs=["be"]),            # bare infinitive verb
    CFGRule(lhs="V-3-S", rhs=["is"]),         # 3rd singular form of a verb
    CFGRule(lhs="V-N-3-S", rhs=["are"]),      # non 3rd singular form of a verb
    CFGRule(lhs="V-PAST", rhs=["expected"]),  # past form of regular verb
    CFGRule(lhs="V-MODAL", rhs=["will"]),     # modal verb
   
    CFGRule(lhs="PP", rhs=["LOC-PP"]),  # preposition phrase
    CFGRule(lhs="PP", rhs=["DIR-PP"]),
    
    CFGRule(lhs="LOC-PP", rhs=["LOC-PRP", "CITY"]),           # perposition for location
    CFGRule(lhs="LOC-PP", rhs=["LOC-PRP", "CONJ-CITY"]),
    CFGRule(lhs="TIME-PP", rhs=["TIME-PRP", "DT-NN-TIME"]),   # preposition for time
    CFGRule(lhs="DIR-PP", rhs=["FROM", "DIR"]),               # preposition for direction
    CFGRule(lhs="NOM-TIME-PP", rhs=["FOR", "NOM-TIME"]),      # preposition for time with determiner
    
    CFGRule(lhs="JJ", rhs=["fair"]),  # adjective
    CFGRule(lhs="JJ", rhs=["light"]),
    CFGRule(lhs="JJ", rhs=["gentle"]),
    CFGRule(lhs="JJ", rhs=["heavy"]),
    CFGRule(lhs="JJ", rhs=["noticeable"]),
    CFGRule(lhs="JJ-WEATHER", rhs=["sunny"]),  # adjective for weather
    
    CFGRule(lhs="GERUND-WIND", rhs=["blowing"]),  # geround

    CFGRule(lhs="NN", rhs=["rain"]),             # noun
    CFGRule(lhs="NN", rhs=["wind"]),
    CFGRule(lhs="NN", rhs=["breeze"]),
    CFGRule(lhs="NNS", rhs=["clouds"]),          # plural noun
    CFGRule(lhs="NN-WEATHER", rhs=["weather"]),  # weather
    CFGRule(lhs="NN-WIND", rhs=["wind"]),        # wind
    
    CFGRule(lhs="QNT-P", rhs=["a lot of"]),      # plural quantifier
    CFGRule(lhs="QNT-P", rhs=["a bit of"]),
    
    CFGRule(lhs="ADV", rhs=["partly"]),  # adverb
    CFGRule(lhs="ADJP", rhs=["ADV", "JJ-WEATHER"]),  # adjective phrase (adverb + adjective)
   
    CFGRule(lhs="DT", rhs=["the"]),  # determiner
            
    CFGRule(lhs="CITY", rhs=["Paris"]),  # proper noun for cities
    CFGRule(lhs="CITY", rhs=["Toulouse"]),
    CFGRule(lhs="CITY", rhs=["Lyon"]),
    CFGRule(lhs="CITY", rhs=["Marseille"]),
    CFGRule(lhs="CITY", rhs=["Nice"]),
    CFGRule(lhs="CITY", rhs=["Bordeaux"]),
    CFGRule(lhs="CITY", rhs=["Montpellier"]),
    
    CFGRule(lhs="PART-OF-DAY-NN", rhs=["morning"]),  # proper noun for part of the day
    CFGRule(lhs="PART-OF-DAY-NN", rhs=["afternoon"]),
    CFGRule(lhs="PART-OF-DAY-NN", rhs=["evening"]),
    CFGRule(lhs="PART-OF-DAY-NN", rhs=["night"]),

    CFGRule(lhs="WEEK-DAYS", rhs=["Monday"]),  # proper noun for days of the week
    CFGRule(lhs="WEEK-DAYS", rhs=["Tuesday"]),
    CFGRule(lhs="WEEK-DAYS", rhs=["Wednesday"]),
    CFGRule(lhs="WEEK-DAYS", rhs=["Thursday"]),
    CFGRule(lhs="WEEK-DAYS", rhs=["Friday"]),
    CFGRule(lhs="WEEK-DAYS", rhs=["Saturday"]),
    CFGRule(lhs="WEEK-DAYS", rhs=["Sunday"]),
    CFGRule(lhs="WEEK-DAYS", rhs=["Sunday"]),
    
    CFGRule(lhs="TIME", rhs=["today"]),  # proper noun for time
    CFGRule(lhs="TIME", rhs=["tomorrow"]),
    CFGRule(lhs="TIME", rhs=["tonight"]),
    
    CFGRule(lhs="DIR", rhs=["North"]),  # proper noun for directions
    CFGRule(lhs="DIR", rhs=["Northeast"]),
    CFGRule(lhs="DIR", rhs=["East"]),
    CFGRule(lhs="DIR", rhs=["Southeast"]),
    CFGRule(lhs="DIR", rhs=["South"]),
    CFGRule(lhs="DIR", rhs=["Southwest"]),
    CFGRule(lhs="DIR", rhs=["West"]),
    CFGRule(lhs="DIR", rhs=["Northwest"]),

    CFGRule(lhs="NOM-TIME", rhs=["TIME"]),  # nominal for time 
    CFGRule(lhs="NOM-TIME", rhs=["TIME-JJ", "WEEK-DAYS"]),  # nominal for time with (adjective + noun)
    
    CFGRule(lhs="TIME-JJ", rhs=["next"]),  # adjective for time
    CFGRule(lhs="TIME-JJ", rhs=["last"]),
    CFGRule(lhs="TIME-JJ", rhs=["coming"]),
    
    CFGRule(lhs="LOC-PRP", rhs=["in"]),   # perposition for location
    CFGRule(lhs="TIME-PRP", rhs=["in"]),  # perposition for time
    CFGRule(lhs="TIME-PRP", rhs=["for"]),
    CFGRule(lhs="TIME-PRP", rhs=["during"]),
    
    CFGRule(lhs="DAY-PRP", rhs=["for"]),    # perposition for day

    CFGRule(lhs="FOR", rhs=["for"]),        # for perposition
    CFGRule(lhs="IN", rhs=["in"]),          # in perposition
    CFGRule(lhs="FROM", rhs=["from"]),      # from perposition
    CFGRule(lhs="TO", rhs=["to"]),          # to perposition
    CFGRule(lhs="DURING", rhs=["during"]),  # during perposition
    
    CFGRule(lhs="NB-ZERO", rhs=["0"]),  # 0
    CFGRule(lhs="NB", rhs=["1"]),       # numbers from 1 to 9
    CFGRule(lhs="NB", rhs=["2"]),  
    CFGRule(lhs="NB", rhs=["3"]),  
    CFGRule(lhs="NB", rhs=["4"]),  
    CFGRule(lhs="NB", rhs=["5"]),  
    CFGRule(lhs="NB", rhs=["6"]),  
    CFGRule(lhs="NB", rhs=["7"]),  
    CFGRule(lhs="NB", rhs=["8"]),  
    CFGRule(lhs="NB", rhs=["9"]),  
    CFGRule(lhs="NB", rhs=["9"]),  
    CFGRule(lhs="NB-SUM", rhs=["NB", "NB"]),  # sum of two numbers
    CFGRule(lhs="NB-SUM", rhs=["NB", "NB-ZERO"]),  
    
    CFGRule(lhs="METRIC", rhs=["km/h"]),  # metric for wind's speed
    CFGRule(lhs="RANGE", rhs=["(", "NB", "TO", "NB-SUM", "METRIC", ")"]),  # range of speed
    
    CFGRule(lhs="CONJ-AND", rhs=["and"]),  # conjunction and
    CFGRule(lhs="CONJ-BUT", rhs=["but"]),  # conjunction but
    CFGRule(lhs="CONJ-CITY", rhs=["CITY", "CONJ-AND", "CITY"]),  # conjunction for combining two cities' names (NP ---> NP and NP)
]
