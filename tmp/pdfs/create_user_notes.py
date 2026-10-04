from pathlib import Path
import arabic_reshaper
from bidi.algorithm import get_display
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from pypdf import PdfReader, PdfWriter
from pypdf.generic import DictionaryObject, NameObject, TextStringObject

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'output/pdf/motmaan-user-notes-ar-rtl.pdf'
OUT.parent.mkdir(parents=True, exist_ok=True)
pdfmetrics.registerFont(TTFont('Arabic', 'C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('ArabicBold', 'C:/Windows/Fonts/arialbd.ttf'))

NOTES = [
('تفضيلات الأطباء وترتيب ظهورهم', 'تسجيل موضوع تفضيلات الطبيب التي تؤثر على ترتيب ظهوره للمريض، والرجوع لاحقًا لتحديد معناها، ومن يضبطها، ومعاييرها وأوزانها، وعلاقتها بأولوية أطباء المركز وإظهار الأطباء الخارجيين عند امتلاء مواعيدهم.'),
('الإلغاء المتأخر وإعادة جدولة الموعد', 'الرجوع لاحقًا لتحديد نتيجة إلغاء المريض بعد المهلة المسموح بها، وقواعد تغيير الموعد وإعادة جدولته وما يترتب عليها ماليًا.'),
('ربط المريض بالطبيب والتغطية البديلة', 'تأجيل تفاصيل إسناد المريض إلى الطبيب، ونقله إلى طبيب آخر، وتغطية الطبيب البديل، وصلاحيات الوصول المرتبطة بهذه الحالات.'),
('التأمين الطبي', 'سؤال صاحب المشروع لاحقًا عن نطاق التأمين: هل المطلوب تسجيل بيانات التغطية والموافقات والمطالبات فقط، أم التكامل الفعلي مع نفيس أو وصيل للتحقق من الأهلية وإدارة الموافقات والمطالبات؟'),
('تحويل رصيد المحفظة إلى حساب بنكي', 'المريض يتواصل مع الإدارة إذا أراد تحويل رصيد محفظة مطمئن إلى حسابه البنكي. تفاصيل المراجعة والموافقة والتنفيذ والمحاسبة تُناقش لاحقًا.'),
('مدة حجز الموعد أثناء الدفع', 'تسجيل موضوع مدة الاحتفاظ المؤقت بالموعد أثناء إتمام الدفع للرجوع إليه لاحقًا. لم تُعتمد مدة محددة.'),
('الحجز عن طريق التحويل البنكي', 'تسجيل سؤال إتاحة الحجز بالدفع عن طريق التحويل البنكي للنقاش لاحقًا. لم تُعتمد آلية للتحقق من التحويل أو تأكيد الحجز به.'),
('صلاحيات الموظفين وإيقاف الطبيب', 'تسجيل تفاصيل جدول صلاحيات الموظفين للرجوع إليها لاحقًا، وكذلك أثر إيقاف حساب الطبيب على مواعيده الحالية والجلسات القائمة وإعادة تفعيله.'),
('نطاق نسب الأطباء وأساس حسابها', 'نسب الأطباء قابلة للتعديل داخل النظام. يُناقش لاحقًا هل تُحدد لكل طبيب أو خدمة أو نطاق آخر، ومن يملك تعديلها، وما أساس الإيراد المستخدم لحساب النسبة.'),
('حقول طلبات توظيف الأطباء ومستنداتها', 'تسجيل تفاصيل الحقول الشخصية والمعلومات المطلوبة في نموذج «انضم إلينا»، وقائمة الشهادات والمستندات الداعمة، للرجوع إليها لاحقًا. المعلومات العامة والخبرات والمؤهلات مطلوبة، لكن القائمة التفصيلية مؤجلة.'),
('ترجمة البيانات العربية المستوردة', 'تسجيل أنواع المحتوى وصيغ الملفات العربية التي ستُترجم إلى الإنجليزية، وكيفية عرض الترجمة، للنقاش لاحقًا. الحاجة إلى الترجمة مسجلة، لكن هذه التفاصيل لم تُحسم.'),
('صلاحيات الأسرة وانتقال الطفل إلى مرحلة البلوغ', 'تأجيل تحديد أنواع البيانات التي يراها أفراد الأسرة والإجراءات المسموح لهم بها. بلوغ الطفل لا يغير الصلاحيات تلقائيًا؛ الإدارة تقرر التغيير، وتفاصيل الإجراء ونطاقه وسجل التعديلات تُناقش لاحقًا.'),
]

W, H = A4
RIGHT, LEFT = W - 48, 48
WIDTH = RIGHT - LEFT
TEAL, INK, GRAY = '#126A67', '#22343A', '#64767D'

def visual(text):
    return get_display(arabic_reshaper.reshape(text), base_dir='R')

def line(c, text, x, y, size=12, bold=False, color=INK):
    c.setFont('ArabicBold' if bold else 'Arabic', size)
    c.setFillColor(HexColor(color))
    c.drawRightString(x, y, visual(text))

def wrap(text, width, size=12, font='Arabic'):
    lines, current = [], ''
    for word in text.split():
        candidate = (current + ' ' + word).strip()
        if current and pdfmetrics.stringWidth(visual(candidate), font, size) > width:
            lines.append(current)
            current = word
        else:
            current = candidate
    if current:
        lines.append(current)
    return lines

def paragraph(c, text, y, size=12, width=WIDTH, leading=19, color=INK):
    for item in wrap(text, width, size):
        line(c, item, RIGHT, y, size, color=color)
        y -= leading
    return y

def header(c, page):
    c.setFillColor(HexColor(TEAL))
    c.rect(0, H - 12, W, 12, fill=1, stroke=0)
    line(c, 'مطمئن | الملاحظات المؤجلة', RIGHT, H - 45, 11, color=TEAL)
    line(c, '٣ أكتوبر ٢٠٢٦', LEFT + 106, H - 45, 10, color=GRAY)
    y = paragraph(c, 'موضوعات طلبت حفظها للرجوع إليها لاحقًا؛ تفاصيلها لا تزال مؤجلة.', H - 83, 11, leading=17, color=GRAY)
    c.setStrokeColor(HexColor('#D9E5E3'))
    c.line(LEFT, 61, RIGHT, 61)
    line(c, f'صفحة {"١" if page == 1 else "٢"} من ٢', RIGHT, 40, 10, color=GRAY)
    line(c, 'المصدر: سجل ملاحظات المستخدم والأسئلة المؤجلة', RIGHT, 78, 9, color=GRAY)
    return y - 22

raw = OUT.with_suffix('.raw.pdf')
c = canvas.Canvas(str(raw), pagesize=A4)
c.setTitle('مطمئن - الملاحظات المؤجلة')
c.setAuthor('Motmaan')
positions = []
for page, start in enumerate([0, 6], 1):
    y = header(c, page)
    for index in range(start, start + 6):
        title, body = NOTES[index]
        numeral = str(index + 1).translate(str.maketrans('0123456789', '٠١٢٣٤٥٦٧٨٩'))
        line(c, f'{numeral}. {title}', RIGHT, y, 13, True, TEAL)
        y -= 23
        y = paragraph(c, body, y, 12, leading=19)
        y -= 19
    positions.append(y)
    if y < 95:
        raise RuntimeError(f'Page content exceeds safe area: {page}, {y}')
    c.showPage()
c.save()
reader = PdfReader(raw)
writer = PdfWriter()
writer.clone_document_from_reader(reader)
writer.root_object[NameObject('/ViewerPreferences')] = DictionaryObject({NameObject('/Direction'): NameObject('/R2L')})
writer.root_object[NameObject('/Lang')] = TextStringObject('ar-SA')
writer.add_metadata({'/Title': 'مطمئن - الملاحظات المسجلة للرجوع إليها لاحقًا', '/Author': 'Motmaan'})
with OUT.open('wb') as stream:
    writer.write(stream)
raw.unlink()
print({'output': str(OUT), 'notes': len(NOTES), 'pages': len(reader.pages), 'bottom_positions': positions})
