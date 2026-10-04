from pathlib import Path

root = Path(__file__).resolve().parents[1]
paths = ['README.md', 'docs/planning/01-system-scope.md', 'docs/planning/05-identity-and-access.md', 'docs/planning/06-decisions-and-open-questions.md', 'docs/planning/10-customer-mobile-appointments.md', 'docs/planning/12-user-notes-and-open-questions.md', 'docs/planning/15-internal-staff-tasks.md', 'docs/handoff/flutter-developer.md', 'docs/handoff/web-frontend-developer.md']
texts = {p: (root / p).read_text(encoding='utf-8') for p in paths}

def replace(path, old, new):
    assert old in texts[path], (path, old)
    texts[path] = texts[path].replace(old, new)

for path in paths:
    replace(path, 'Updated: 3 October 2026.', 'Updated: 4 October 2026.') if 'Updated: 3 October 2026.' in texts[path] else replace(path, 'Updated: 2 October 2026.', 'Updated: 4 October 2026.')

future = 'Changes to recurring patient tasks apply only to future occurrences and preserve earlier completion history.'
direct = 'Doctors may issue finalized clinical reports and prescriptions directly, without a separate management approval step, within granted permissions, assigned-patient scope, and applicable qualifications.'
tasks = 'Internal tasks close automatically once the required completion condition is met, without creator approval; the multi-assignee completion condition remains open. Staff notifications are retained in an unread list, including events missed while the website was closed.'

for path in ['docs/planning/01-system-scope.md', 'docs/handoff/flutter-developer.md', 'docs/handoff/web-frontend-developer.md']:
    replace(path, 'Numeric limits, schedule-edit effects, and weekly summaries remain open.', future + ' Numeric limits and weekly summaries remain open.') if 'Numeric limits, schedule-edit effects, and weekly summaries remain open.' in texts[path] else replace(path, 'numeric limits, schedule-edit effects, and weekly summaries remain open.', future + ' Numeric limits and weekly summaries remain open.')

replace('docs/planning/10-customer-mobile-appointments.md', 'Numeric defaults/limits, task-edit effects on existing occurrences, and weekly-summary behavior remain open.', future + ' Numeric defaults/limits and weekly-summary behavior remain open.')
replace('docs/handoff/flutter-developer.md', 'Numeric patient-task schedule limits, effects of task edits, and weekly-summary behavior;', 'Numeric patient-task schedule limits and weekly-summary behavior;')
replace('docs/handoff/web-frontend-developer.md', 'Patient-task schedule limits/edit effects, weekly summaries,', 'Patient-task schedule limits, weekly summaries,')
replace('docs/handoff/web-frontend-developer.md', 'Numeric schedule limits and edit effects remain open.', future + ' Numeric schedule limits remain open.')
replace('docs/handoff/web-frontend-developer.md', 'clinical qualification/approval rules.', 'clinical qualification rules; direct report/prescription issuance is confirmed.')
for path in ['docs/planning/01-system-scope.md', 'docs/planning/05-identity-and-access.md', 'docs/handoff/web-frontend-developer.md', 'docs/handoff/flutter-developer.md']:
    texts[path] += '\n## Confirmed clarification - 4 October 2026\n\n- ' + direct + '\n'
    if path.endswith('flutter-developer.md'):
        texts[path] += '- ' + future + ' Display API-provided task versions and preserve historical progress.\n'
    if path.endswith('web-frontend-developer.md'):
        texts[path] += '- ' + tasks + ' Transport and detailed recipient rules remain open.\n'

p = 'docs/planning/15-internal-staff-tasks.md'
replace(p, '- Status changes happen automatically from task actions.', '- Tasks close automatically after the required completion condition is met, without a creator approval step. Whether all assignees must finish remains open.\n- Staff notifications persist in an unread list, including events missed while the website is closed.\n- Status changes happen automatically from task actions.')
replace(p, 'Live website notifications are confirmed; transport technology, persistent unread history, reconnect behavior, and notifications while the website is closed remain undecided.', 'Live website notifications and persistent unread history, including events missed while the website is closed, are confirmed. Transport technology and reconnect behavior remain open.')
replace(p, 'whole-task completion, reassignment, and completion approval.', 'whole-task completion condition, and reassignment. Creator approval is not required.')
replace(p, 'notification recipients, persistent unread history, and escalation.', 'notification recipients and escalation. Persistent unread history is confirmed.')

p = 'docs/planning/06-decisions-and-open-questions.md'
replace(p, '| Doctor clinical scope | Doctors are expected', '| Direct clinical issuance | ' + direct + ' |\n| Doctor clinical scope | Doctors are expected')
replace(p, '| Patient tasks | Doctors control', '| Patient-task edits | ' + future + ' |\n| Patient tasks | Doctors control')
replace(p, '| Internal staff tasks | Reception/accountant', '| Internal-task completion and notifications | ' + tasks + ' |\n| Internal staff tasks | Reception/accountant')
replace(p, 'changes to existing occurrences, and weekly summaries.', 'weekly summaries, and detailed treatment-task limits. Future-only edits with preserved earlier history are confirmed.')
replace(p, 'multi-assignee completion/approval, notification persistence/recipients,', 'multi-assignee completion condition, notification recipients,')
texts[p] += '\n## Owner-message revision - 4 October 2026\n\nThe user resolved automatic task closure without creator approval, persistent unread staff notifications, future-only patient-task edits with preserved history, and direct finalized clinical report/prescription issuance. The revised owner questions are in the tracker. Package-stop refunds, support hours/response targets, the SMS provider, and detailed staff permissions/deactivation were removed from this owner message only; they remain unresolved or previously deferred. Package family sharing is now explicitly included in the owner question. Preparing this message does not answer or change the deferred status of the other questions.\n'

p = 'docs/planning/12-user-notes-and-open-questions.md'
replace(p, 'Numeric limits, effects of task edits, and weekly summaries remain open.', future + ' Numeric limits and weekly summaries remain open.')
replace(p, 'Notification persistence/recipients and file constraints remain open.', 'Unread notification persistence, including events missed while the website was closed, is confirmed. Recipient rules and file constraints remain open.')
replace(p, 'Status is automatic from actions; exact mappings and multi-assignee completion remain open.', 'Status is automatic from actions. Tasks close automatically when the completion condition is met, without creator approval; exact mappings and the multi-assignee completion condition remain open.')
replace(p, 'within granted permissions, assigned-patient scope, and applicable qualification rules.\n- Percentage compensation', 'within granted permissions, assigned-patient scope, and applicable qualification rules. ' + direct + '\n- Percentage compensation')
start = texts[p].index('## Next ten questions')
end = texts[p].index('## Deferred by the user', start)
texts[p] = texts[p][:start] + '''## Next ten questions

The current queue has three items after the 4 October answers and owner-message removals. The owner-facing version below also includes selected previously deferred topics; their answers are still pending.

1. What are the internal multi-assignee task details, including whether all assignees must complete their parts or one assignee can complete the task for everyone? Multiple assignees remain a confirmed requirement; the owner message asks about support and details.
2. What are the full details of the system's assessment/test platform, including tests, patient usage, results, and available integration?
3. Can a package contain different services, can patients choose any eligible doctor, and can the package be shared among family members?

### Resolved on 4 October 2026

- Internal tasks close automatically after the required completion condition is met; creator approval is not required. The multi-assignee completion condition remains open.
- Retain staff notifications in an unread list, including events missed while the website was closed.
- Changes to recurring patient tasks apply only to future occurrences and preserve earlier completion history.
- Doctors can issue finalized clinical reports and prescriptions directly, within their permissions, assigned-patient scope, and qualifications, without a separate management approval step.

### Removed from this owner message, still unresolved

- Stopping an already-started package and refunding unused sessions.
- Support working hours, response targets, and urgent-ticket targets.
- Existing SMS provider and available integration access.
- Detailed staff permission matrix and doctor-deactivation effects; these retain their prior deferred status.

## Revised owner questions - 4 October 2026

1. هل النظام يدعم إسناد المهمة الداخلية لأكثر من موظف؟ وما تفاصيل إنشاء المهمة وإسنادها ومتابعتها وإتمامها؟
2. ما تفاصيل منصة الاختبارات المرتبطة بالنظام: اسمها، والاختبارات المتاحة، وطريقة استخدامها وعرض النتائج، وإمكانية الربط معها؟
3. هل الباقة تشمل خدمات مختلفة؟ وهل يختار المريض أي طبيب مناسب؟ وهل يمكن مشاركة الباقة بين أفراد الأسرة؟
4. ما التفضيلات التي تحدد ترتيب ظهور الأطباء للمريض؟ ومن يضبطها؟
5. ما سياسة الإلغاء المتأخر وإعادة جدولة الموعد؟
6. كيف يُحدد طبيب المريض، وكيف يُنقل إلى طبيب آخر أو يُعين له طبيب بديل؟
7. هل المطلوب في التأمين تسجيل البيانات فقط، أم الربط مع نفيس أو وصيل؟ وما العمليات المطلوبة؟
8. ما خطوات تحويل رصيد محفظة المريض إلى حسابه البنكي؟ ومن يوافق على التحويل؟
9. عند اختيار موعد وبدء الدفع، كم دقيقة يظل الموعد محجوزًا قبل إتاحته لشخص آخر إذا لم يكتمل الدفع؟
10. هل نسمح بالحجز عن طريق التحويل البنكي؟ وإذا نعم، كيف يُتحقق من التحويل ويُؤكد الحجز؟
11. ما تفاصيل نسب الأطباء: هل تختلف حسب الطبيب أو الخدمة؟ وعلى أي مبلغ تُحسب؟ وكيف تُعامل الخصومات والضرائب والباقات والاستردادات؟ ومن يملك تعديل النسبة؟
12. ما البيانات والشهادات والمستندات المطلوبة من الطبيب في نموذج «انضم إلينا»؟
13. ما البيانات والملفات العربية المطلوب ترجمتها للإنجليزية؟ وكيف تُعرض الترجمة؟
14. ما تفاصيل الربط العائلي كاملة: من يضيف أفراد الأسرة، وكيف يُثبت الربط، وما الذي يراه أو ينفذه كل فرد، وكيف يُفك الربط أو تتغير الصلاحيات عند بلوغ الطفل؟
15. ما قائمة مجالات خبرة الأطباء التي نعتمدها ليختار منها الطبيب ويستخدمها المريض في البحث؟ نحتاج أسماءها بالعربية والإنجليزية.

''' + texts[p][end:]

texts['README.md'] += '\n## Confirmed clarification - 4 October 2026\n\n- ' + tasks + '\n- ' + future + '\n- ' + direct + '\n- The owner-facing question list was revised in the user tracker; removed questions remain unresolved or explicitly deferred. No implementation is authorized.\n'

for path, text in texts.items():
    (root / path).write_text(text, encoding='utf-8')
print('Updated planning tracker, decision register, relevant topic files, and both developer handoffs.')
