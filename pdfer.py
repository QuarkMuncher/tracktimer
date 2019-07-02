import database as db
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from time import mktime
from datetime import datetime

# Move this to init
# LIST_STYLE = TableStyle(
#     [
#         ("LINEABOVE", (0, 0), (-1, 0), 2, colors.green),
#         ("LINEABOVE", (0, 1), (-1, -1), 0.25, colors.black),
#         ("LINEBELOW", (0, -1), (-1, -1), 2, colors.green),
#         ("ALIGN", (1, 1), (-1, -1), "RIGHT"),
#     ]
# )


class statexport:
    def __init__(self):
        self.style = getSampleStyleSheet()
        self.custom_header1 = self.style["Heading1"]
        self.custom_header1.fontSize = 40
        self.custom_header1.leading = 40
        self.custom_body = self.style["BodyText"]
        self.custom_body.fontSize = 12

    def extract_information(self, path, begin, end):
        begin_doc = begin.replace("/", "-")
        end_doc = end.replace("/", "-")
        my_doc = SimpleDocTemplate(f"{begin_doc} - {end_doc}.pdf")
        begin = mktime(datetime.strptime(begin, "%Y/%m/%d").timetuple())
        end = mktime(datetime.strptime(end, "%Y/%m/%d").timetuple())
        reports = db.report_range(begin, end)

        header = Paragraph("Abekat", self.custom_header1)
        flowables = []

        flowables.append(header)
        flowables.append(Paragraph("fisk", self.style["BodyText"]))
        my_doc.build(flowables)

        print(my_doc)
        return my_doc


path = "reportlab-sample.pdf"
exp = statexport()
begin, end = "1980/01/01", "2019/07/01"
print(exp.extract_information(path, begin, end))
