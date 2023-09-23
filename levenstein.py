import numpy as np
class Levenstein:
    def __init__(self):
        pass
    def Algo(self,var1,var2):
        distance_matrix = np.zeros((len(var1)+1,len(var2)+1),dtype=int)
        for i in range(len(var1)+1):
            distance_matrix[i][0] = i
        for j in range(len(var2)+1):
            distance_matrix[0][j] = j
        return self.similarity(var1,var2,distance_matrix)
    def Print_Matrix(self,matrix,rows,cols):
        for i in range(rows+1):
            for j in range(cols+1):
                print(matrix[i][j],end=' ')
            print()
    def similarity(self,var1,var2,matrix):
        distance = 0
        a, b, c = 0, 0, 0
        for i in range(len(var1)):
            for j in range(len(var2)):
                if var1[i] == var2[j]:
                    matrix[i+1][j+1] = matrix[i][j]
                else:
                    a = matrix[i+1][j]
                    b = matrix[i][j+1]
                    c = matrix[i][j]
                    matrix[i+1][j+1] = min([a,b,c])+1
        distance = matrix[len(var1)][len(var2)]
        # self.Print_Matrix(matrix,len(var1),len(var2))
        return distance
Algorithm = Levenstein()
def Implement(query):
    d1 = "Namal University is an institution of higher education located in Mianwali, Punjab, Pakistan. The university is committed to proactively seeking out and developing brilliant students regardless of their socio-economic backgrounds. Namal University is a community of people with diverse talents, interests, ethnicities, and cultures. The university transforms its students for a lifetime of learning and equips them with skills to bring innovation in their respective fields and communities1. Social impact is one of the key values at Namal, and students uphold the spirit of giving back to society through various programs of community service1."
    d2 = 'The Numl University(National University of Modern Languages) is a multi-campus public university located in Islamabad, Pakistan, with other campuses in different cities of Pakistan. NUML was established as an institute in 1969 to help people communicate and understand each other in different oriental and occidental languages, to assimilate different cultures, and to act as a springboard for emerging disciplines12. The university has a vision to become a leading institution in creating knowledge and competencies for inclusive developments, and its mission is to foster creative pedagogy, innovative research, and inclusive communication1.'
    d3 = "COMSATS University Islamabad (CUI), formerly known as COMSATS Institute of Information Technology (CIIT), is a public university in Pakistan. It is a multi-campus university with its principal seat located in Islamabad. COMSATS was envisioned as Pakistan’s first exclusive Institute of Information Technology. In the latest QS University Rankings, CUI ranked 7th in Pakistan and 801-1000 in the world. Nationally, it is ranked top-most in the Computer Sciences and IT category12. The origins of CUI date back to 1998, and the university is one of the leading universities of Pakistan with five broad faculties including Engineering, Information Science and Technology, Business Administration, and Architecture and Design. It has more than 36,000 students and offers 100-degree programs1."
    Documents = [d1,d3,d2]
    D_Distance = []
    similars = []
    for document in Documents:
        min_distance = float('inf')
        min_index = -1
        for i in range(len(document) - len(query) + 1):
            substring = document[i:i+len(query)]
            distance = Algorithm.Algo(substring, query)
            if distance < min_distance:
                min_distance = distance
                min_index = i
        similar = document[min_index:min_index+len(query)]
        similars.append(similar)
        D_Distance.append(min_distance)
    D_indices = []
    D_Distance_sorted = sorted(D_Distance)
    for element in D_Distance_sorted:
        for i in range(len(D_Distance)):
            if element == D_Distance[i] and i not in D_indices:
                D_indices.append(i)
                break
    output = "\n \n\n\n \n"
    for d in range(len(D_Distance)):
        output += "✦"
        output += Documents[D_indices[d]]
        output += "\n                    \n      \n"
    return output