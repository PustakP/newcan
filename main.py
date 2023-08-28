from bs4 import BeautifulSoup
#pp

html = """

 <tr>
    <td class="SSSWEEKLYTIMEBACKGROUND" rowspan="1"><span class="SSSTEXTWEEKLYTIME">8:00AM</span></td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="SSSWEEKLYBACKGROUND" rowspan="1"><span class="SSSTEXTWEEKLY">MED MED201 - L1<br>Lecture<br>8:00AM -
        9:25AM<br>S. Floor D Block D217</span></td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
  </tr>
  <tr>
    <td class="SSSWEEKLYTIMEBACKGROUND" rowspan="1"><span class="SSSTEXTWEEKLYTIME">9:00AM</span></td>
    <td class="SSSWEEKLYBACKGROUND" rowspan="2"><span class="SSSTEXTWEEKLY">CSD CSD101 - L1<br>Lecture<br>9:30AM -
        10:55AM<br>T. Floor B Block B315</span></td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="SSSWEEKLYBACKGROUNDOVLP" rowspan="1"><span class="SSSTEXTWEEKLY">MED MED201 - L1<br>Lecture<br>8:00AM -
        9:25AM<br>S. Floor D Block D217
        <hr width="75%" class="PSHORIZONTALRULE">CSD CSD101 - L1<br>Lecture<br>9:30AM - 10:55AM<br>T. Floor B Block B315
      </span></td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="SSSWEEKLYBACKGROUND" rowspan="2"><span class="SSSTEXTWEEKLY">MED MED201 - L1<br>Lecture<br>9:30AM -
        10:55AM<br>S. Floor D Block D217</span></td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
  </tr>
  <tr>
    <td class="SSSWEEKLYTIMEBACKGROUND" rowspan="1"><span class="SSSTEXTWEEKLYTIME">10:00AM</span></td>
    <td class="SSSWEEKLYBACKGROUND" rowspan="2"><span class="SSSTEXTWEEKLY">MAT MAT103 - L1<br>Lecture<br>10:30AM -
        11:55AM<br>T. Floor B Block B315</span></td>
    <td class="SSSWEEKLYBACKGROUND" rowspan="1"><span class="SSSTEXTWEEKLY">CSD CSD101 - L1<br>Lecture<br>9:30AM -
        10:55AM<br>T. Floor B Block B315</span></td>
    <td class="SSSWEEKLYBACKGROUND" rowspan="2"><span class="SSSTEXTWEEKLY">MAT MAT103 - L1<br>Lecture<br>10:30AM -
        11:55AM<br>T. Floor B Block B315</span></td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
  </tr>
  <tr>
    <td class="SSSWEEKLYTIMEBACKGROUND" rowspan="1"><span class="SSSTEXTWEEKLYTIME">11:00AM</span></td>
    <td class="SSSWEEKLYBACKGROUND" rowspan="1"><span class="SSSTEXTWEEKLY">PHY PHY101 - L3<br>Lecture<br>11:00AM -
        11:55AM<br>F. Floor D Block D102</span></td>
    <td class="SSSWEEKLYBACKGROUND" rowspan="1"><span class="SSSTEXTWEEKLY">PHY PHY101 - L3<br>Lecture<br>11:00AM -
        11:55AM<br>F. Floor D Block D102</span></td>
    <td class="SSSWEEKLYBACKGROUND" rowspan="1"><span class="SSSTEXTWEEKLY">PHY PHY101 - L3<br>Lecture<br>11:00AM -
        11:55AM<br>F. Floor D Block D102</span></td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
  </tr>
  <tr>
    <td class="SSSWEEKLYTIMEBACKGROUND" rowspan="1"><span class="SSSTEXTWEEKLYTIME">12:00PM</span></td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
  </tr>
  <tr>
    <td class="SSSWEEKLYTIMEBACKGROUND" rowspan="1"><span class="SSSTEXTWEEKLYTIME">1:00PM</span></td>
    <td class="SSSWEEKLYBACKGROUND" rowspan="2"><span class="SSSTEXTWEEKLY">CSD CSD101 - P2<br>Practicum<br>1:00PM -
        2:55PM<br>T. Floor D Block D313</span></td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
  </tr>
  <tr>
    <td class="SSSWEEKLYTIMEBACKGROUND" rowspan="1"><span class="SSSTEXTWEEKLYTIME">2:00PM</span></td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
  </tr>
  <tr>
    <td class="SSSWEEKLYTIMEBACKGROUND" rowspan="1"><span class="SSSTEXTWEEKLYTIME">3:00PM</span></td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="SSSWEEKLYBACKGROUND" rowspan="2"><span class="SSSTEXTWEEKLY">MED MED201 - P4<br>Practicum<br>3:00PM -
        4:55PM<br>G. Floor C Block C013</span></td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
  </tr>
  <tr>
    <td class="SSSWEEKLYTIMEBACKGROUND" rowspan="1"><span class="SSSTEXTWEEKLYTIME">4:00PM</span></td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
  </tr>
  <tr>
    <td class="SSSWEEKLYTIMEBACKGROUND" rowspan="1"><span class="SSSTEXTWEEKLYTIME">5:00PM</span></td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
  </tr>
  <tr>
    <td class="SSSWEEKLYTIMEBACKGROUND" rowspan="1"><span class="SSSTEXTWEEKLYTIME">6:00PM</span></td>
    <td class="SSSWEEKLYBACKGROUND" rowspan="1"><span class="SSSTEXTWEEKLY">PHY PHY101 - T4<br>Tutorial<br>6:00PM -
        6:55PM<br>T. Floor D Block D306</span></td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="SSSWEEKLYBACKGROUND" rowspan="1"><span class="SSSTEXTWEEKLY">MAT MAT103 - T4<br>Tutorial<br>6:00PM -
        6:55PM<br>S. Floor B Block B219</span></td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
    <td class="PSLEVEL3GRID">&nbsp;</td>
  </tr>
  </tbody>
  </table>
  </div>


"""


soup = BeautifulSoup(html, 'html.parser')

schedule = {}

# Find all rows in the table
rows = soup.find_all('tr')

# Iterate through each row and extract data
for row in rows:
    columns = row.find_all('td')

    # Skip rows with no data
    if len(columns) == 0:
        continue

    time = columns[0].find('span', class_='SSSTEXTWEEKLYTIME').text

    # Initialize the schedule for the current time slot
    schedule[time] = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": []
    }

    # Extract class information for each day
    for i in range(1, len(columns)):
        class_info = columns[i].find('span', class_='SSSTEXTWEEKLY')
        if class_info:
            classes = [class_.strip() for class_ in class_info.text.split('<hr>')]
            day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"][i - 1]
            schedule[time][day] = classes

# Print the parsed schedule
for time, classes in schedule.items():
    print(f"{time}:")
    for day, class_list in classes.items():
        if class_list:
            print(f"  {day}: {', '.join(class_list)}")