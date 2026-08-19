const modes = {
  audit: {
    label: 'AUDIT MODE', type: 'OBSERVABLE CONDITIONS', tone: 'Evidence before backlog', headline: 'What must be true before we call this finished?', copy: 'Define three to six conditions an independent observer can check without asking for interpretation.', status: 'READY', risk: 'VAGUE', result: 'ROADMAP', description: 'Start with the condition, not the backlog.'
  },
  sequence: {
    label: 'SEQUENCE MODE', type: 'BROKEN / MISSING', tone: 'Dependencies before motion', headline: 'Which work actually unlocks the next proof?', copy: 'Derive only evidence-backed tasks, split them until they fail independently, and order them by dependency.', status: 'ORDERED', risk: 'HIDDEN', result: 'CRITICAL PATH', description: 'A shorter roadmap is useful when it is true.'
  },
  verify: {
    label: 'VERIFY MODE', type: 'DONE / BLOCKED', tone: 'Outcome before status', headline: 'What did the live system prove?', copy: 'Recheck every finish-line condition independently. Preserve a real blocker instead of manufacturing completion.', status: 'PROVEN', risk: 'VISIBLE', result: 'PASS / STOP', description: 'Completion is an observed outcome, not a task label.'
  }
};

function applyMode(id) {
  const mode = modes[id];
  if (!mode) return;
  const values = {
    '[data-preview-label]': mode.label,
    '[data-preview-type]': mode.type,
    '[data-preview-tone]': mode.tone,
    '[data-preview-headline]': mode.headline,
    '[data-preview-copy]': mode.copy,
    '[data-preview-status]': mode.status,
    '[data-preview-risk]': mode.risk,
    '[data-preview-result]': mode.result,
    '[data-preview-description]': mode.description
  };
  Object.entries(values).forEach(([selector, value]) => document.querySelectorAll(selector).forEach((node) => { node.textContent = value; }));
  document.querySelectorAll('.brand-option').forEach((button) => {
    const selected = button.dataset.mode === id;
    button.classList.toggle('is-active', selected);
    button.setAttribute('aria-selected', String(selected));
    button.tabIndex = selected ? 0 : -1;
  });
}

function moveSelection(current, offset) {
  const buttons = Array.from(document.querySelectorAll('.brand-option'));
  const index = buttons.indexOf(current);
  if (index < 0) return;
  const next = buttons[(index + offset + buttons.length) % buttons.length];
  next.focus();
  applyMode(next.dataset.mode);
}

document.querySelectorAll('.brand-option').forEach((button) => {
  button.addEventListener('click', () => applyMode(button.dataset.mode));
  button.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowDown' || event.key === 'ArrowRight') { event.preventDefault(); moveSelection(button, 1); }
    if (event.key === 'ArrowUp' || event.key === 'ArrowLeft') { event.preventDefault(); moveSelection(button, -1); }
    if (event.key === 'Home') { event.preventDefault(); const first = document.querySelector('.brand-option'); first?.focus(); if (first) applyMode(first.dataset.mode); }
    if (event.key === 'End') { event.preventDefault(); const buttons = document.querySelectorAll('.brand-option'); const last = buttons[buttons.length - 1]; last?.focus(); if (last) applyMode(last.dataset.mode); }
  });
});

applyMode('audit');
