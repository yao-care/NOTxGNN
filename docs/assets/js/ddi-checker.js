/**
 * NOTxGNN Drug-Drug Interaction Checker
 *
 * Client-side DDI checking with 15 built-in curated rules (DDInter consulted as a reference; not a full database lookup).
 * Provides real-time interaction alerts for drug repurposing candidates.
 *
 * @author NOTxGNN Team
 * @version 1.0.0
 */
(function(global) {
  'use strict';

  const CONFIG = {
    // This site does not publish /data/ddi-index.json; only the curated rules
    // below are used. Set a URL here once such a file exists.
    ddiDataUrl: null,
    maxAlerts: 10
  };

  // Severity levels with priority (higher = more severe)
  const SEVERITY = {
    'Major': { priority: 3, class: 'ddi-major', label: 'Alvorlig' },
    'Moderate': { priority: 2, class: 'ddi-moderate', label: 'Moderat' },
    'Minor': { priority: 1, class: 'ddi-minor', label: 'Mindre' }
  };

  // 15 built-in high-priority DDI rules (hand-curated, DDInter consulted as a reference)
  // Format: { drug1: [synonym list], drug2: [synonym list], severity, summary, detail }
  const CURATED_DDI_RULES = [
    {
      drugs: [
        ['warfarin', 'coumadin'],
        ['ibuprofen', 'advil', 'motrin', 'brufen']
      ],
      severity: 'Major',
      summary: 'Warfarin + Ibuprofen: økt blødningsrisiko',
      detail: 'NSAID-er hemmer blodplatefunksjonen og kan forsterke den antikoagulerende effekten av warfarin, noe som øker risikoen for blødning i mage-tarmkanalen betydelig.',
      recommendation: 'Bruk paracetamol i stedet, eller legg til en protonpumpehemmer som mageslimhinnebeskyttelse.'
    },
    {
      drugs: [
        ['warfarin', 'coumadin'],
        ['aspirin', 'acetylsalicylic acid']
      ],
      severity: 'Major',
      summary: 'Warfarin + Acetylsalisylsyre: økt blødningsrisiko',
      detail: 'Begge påvirker hemostasen; samtidig bruk øker blødningsrisikoen kraftig.',
      recommendation: 'Hvis kombinasjonen er nødvendig, bruk lavdose acetylsalisylsyre og følg INR tett.'
    },
    {
      drugs: [
        ['warfarin', 'coumadin'],
        ['naproxen', 'aleve', 'naprosyn']
      ],
      severity: 'Major',
      summary: 'Warfarin + Naproksen: økt blødningsrisiko',
      detail: 'Naproksen sammen med warfarin øker risikoen for blødning i mage-tarmkanalen og andre blødninger.',
      recommendation: 'Bruk paracetamol mot smerter i stedet.'
    },
    {
      drugs: [
        ['metformin', 'glucophage'],
        ['iodixanol', 'visipaque', 'iopamidol', 'isovue', 'contrast']
      ],
      severity: 'Major',
      summary: 'Metformin + jodholdige kontrastmidler: risiko for laktacidose',
      detail: 'Kontrastmidler kan gi akutt nyreskade, slik at metformin hoper seg opp og laktacidose kan oppstå.',
      recommendation: 'Stopp metformin 48 timer før undersøkelsen, og start igjen først når normal nyrefunksjon er bekreftet.'
    },
    {
      drugs: [
        ['colchicine', 'colcrys'],
        ['clarithromycin', 'biaxin', 'klacid']
      ],
      severity: 'Major',
      summary: 'Kolkisin + Klaritromycin: risiko for toksisitet',
      detail: 'Klaritromycin er en sterk CYP3A4-hemmer og øker blodkonsentrasjonen av kolkisin kraftig.',
      recommendation: 'Unngå kombinasjonen eller reduser kolkisindosen betydelig.'
    },
    {
      drugs: [
        ['colchicine', 'colcrys'],
        ['ritonavir', 'norvir', 'cobicistat', 'tybost']
      ],
      severity: 'Major',
      summary: 'Kolkisin + HIV-proteasehemmere: risiko for alvorlig toksisitet',
      detail: 'HIV-proteasehemmere øker kolkisinkonsentrasjonen markert og kan gi dødelig forgiftning.',
      recommendation: 'Kontraindisert hos pasienter med nedsatt nyre- eller leverfunksjon.'
    },
    {
      drugs: [
        ['simvastatin', 'zocor'],
        ['amiodarone', 'cordarone']
      ],
      severity: 'Major',
      summary: 'Simvastatin + Amiodaron: risiko for myopati',
      detail: 'Amiodaron øker simvastatinkonsentrasjonen og dermed risikoen for rabdomyolyse.',
      recommendation: 'Ikke overskrid simvastatin 20 mg/døgn, eller bytt til et annet statin.'
    },
    {
      drugs: [
        ['fluoxetine', 'prozac', 'sertraline', 'zoloft', 'paroxetine', 'paxil'],
        ['tramadol', 'ultram']
      ],
      severity: 'Major',
      summary: 'SSRI + Tramadol: risiko for serotonergt syndrom',
      detail: 'Begge øker den serotonerge aktiviteten; samtidig bruk kan gi livstruende serotonergt syndrom.',
      recommendation: 'Følg tett med på symptomer (hypertermi, myoklonus, endret mental status) og vurder et annet smertestillende middel.'
    },
    {
      drugs: [
        ['fluoxetine', 'prozac', 'sertraline', 'zoloft', 'paroxetine', 'paxil'],
        ['linezolid', 'zyvox']
      ],
      severity: 'Major',
      summary: 'SSRI + Linezolid: risiko for serotonergt syndrom',
      detail: 'Linezolid er en MAO-hemmer; kombinasjon med SSRI er svært farlig.',
      recommendation: 'Unngå kombinasjonen. Hvis linezolid er nødvendig, stopp SSRI og hold en passende utvaskingsperiode.'
    },
    {
      drugs: [
        ['amiodarone', 'cordarone'],
        ['moxifloxacin', 'avelox']
      ],
      severity: 'Major',
      summary: 'Amiodaron + Moksifloksacin: risiko for QT-forlengelse',
      detail: 'Begge kan forlenge QT-tiden; samtidig bruk øker risikoen for torsades de pointes.',
      recommendation: 'Unngå kombinasjonen eller følg EKG tett.'
    },
    {
      drugs: [
        ['digoxin', 'lanoxin'],
        ['amiodarone', 'cordarone']
      ],
      severity: 'Major',
      summary: 'Digoksin + Amiodaron: risiko for digoksinforgiftning',
      detail: 'Amiodaron øker blodkonsentrasjonen av digoksin med omtrent 70%.',
      recommendation: 'Ved oppstart av amiodaron: halver digoksindosen og følg blodkonsentrasjonen.'
    },
    {
      drugs: [
        ['clopidogrel', 'plavix'],
        ['omeprazole', 'prilosec', 'esomeprazole', 'nexium']
      ],
      severity: 'Moderate',
      summary: 'Klopidogrel + PPI: redusert platehemmende effekt',
      detail: 'Omeprazol hemmer CYP2C19 og reduserer omdannelsen av klopidogrel til aktiv metabolitt.',
      recommendation: 'Vurder pantoprazol eller en H2-blokker i stedet.'
    },
    {
      drugs: [
        ['lithium', 'lithobid'],
        ['ibuprofen', 'advil', 'naproxen', 'aleve', 'diclofenac']
      ],
      severity: 'Major',
      summary: 'Litium + NSAID-er: risiko for litiumforgiftning',
      detail: 'NSAID-er reduserer utskillelsen av litium via nyrene og øker blodkonsentrasjonen.',
      recommendation: 'Unngå kombinasjonen eller følg litiumkonsentrasjonen tett.'
    },
    {
      drugs: [
        ['potassium', 'k-dur', 'klor-con'],
        ['spironolactone', 'aldactone', 'eplerenone', 'inspra']
      ],
      severity: 'Major',
      summary: 'Kaliumtilskudd + kaliumsparende diuretika: risiko for hyperkalemi',
      detail: 'Begge øker serumkalium; samtidig bruk kan gi livstruende hyperkalemi.',
      recommendation: 'Kontroller serumkalium regelmessig og unngå samtidig kaliumtilskudd.'
    },
    {
      drugs: [
        ['methotrexate', 'trexall'],
        ['trimethoprim', 'bactrim', 'septra', 'sulfamethoxazole']
      ],
      severity: 'Major',
      summary: 'Metotreksat + Trimetoprim-sulfametoksazol: risiko for benmargssuppresjon',
      detail: 'Begge hemmer folatmetabolismen; samtidig bruk øker risikoen for benmargssuppresjon og mukositt.',
      recommendation: 'Unngå kombinasjonen, eller sørg for tilstrekkelig folattilskudd og følg blodverdiene tett.'
    }
  ];

  let ddiIndex = null;
  let isLoaded = false;

  /**
   * Load DDI index data
   */
  async function loadDDIIndex() {
    if (isLoaded) return;
    if (!CONFIG.ddiDataUrl) {
      isLoaded = true;
      return;
    }

    try {
      const response = await fetch(CONFIG.ddiDataUrl);
      if (response.ok) {
        ddiIndex = await response.json();
        isLoaded = true;
        console.log('DDI index loaded:', ddiIndex?.count || 0, 'interactions');
      }
    } catch (error) {
      console.warn('DDI index not available, using curated rules only');
      isLoaded = true;
    }
  }

  /**
   * Normalize drug name for comparison
   */
  function normalizeDrugName(name) {
    if (!name) return '';
    return name.toLowerCase()
      .replace(/\s+/g, ' ')
      .replace(/[^a-z0-9\s]/g, '')
      .trim();
  }

  /**
   * Check if a drug name matches any of the synonyms
   */
  function matchesDrug(drugName, synonyms) {
    const normalized = normalizeDrugName(drugName);
    return synonyms.some(syn => {
      const normalizedSyn = normalizeDrugName(syn);
      return normalized.includes(normalizedSyn) || normalizedSyn.includes(normalized);
    });
  }

  /**
   * Check for DDI between two drugs using curated rules
   */
  function checkCuratedDDI(drug1, drug2) {
    const alerts = [];

    for (const rule of CURATED_DDI_RULES) {
      const [drugGroup1, drugGroup2] = rule.drugs;

      // Check if drug1 matches group1 and drug2 matches group2, or vice versa
      if (
        (matchesDrug(drug1, drugGroup1) && matchesDrug(drug2, drugGroup2)) ||
        (matchesDrug(drug1, drugGroup2) && matchesDrug(drug2, drugGroup1))
      ) {
        alerts.push({
          drug1: drug1,
          drug2: drug2,
          severity: rule.severity,
          severityInfo: SEVERITY[rule.severity],
          summary: rule.summary,
          detail: rule.detail,
          recommendation: rule.recommendation,
          source: 'Innebygde interaksjonsregler i NOTxGNN (15 utvalgte regler; ikke et fullstendig DDInter-oppslag)'
        });
      }
    }

    return alerts;
  }

  /**
   * Check DDI for a list of medications
   * @param {string[]} medications - Array of medication names
   * @returns {Object[]} Array of DDI alerts
   */
  function checkInteractions(medications) {
    if (!medications || medications.length < 2) {
      return [];
    }

    const allAlerts = [];
    const seen = new Set();

    // Check all pairs
    for (let i = 0; i < medications.length; i++) {
      for (let j = i + 1; j < medications.length; j++) {
        const drug1 = medications[i];
        const drug2 = medications[j];
        const pairKey = [drug1, drug2].sort().join('|');

        if (seen.has(pairKey)) continue;
        seen.add(pairKey);

        const alerts = checkCuratedDDI(drug1, drug2);
        allAlerts.push(...alerts);
      }
    }

    // Sort by severity (highest first) and limit
    return allAlerts
      .sort((a, b) => b.severityInfo.priority - a.severityInfo.priority)
      .slice(0, CONFIG.maxAlerts);
  }

  /**
   * Check if a new drug has interactions with existing medications
   * @param {string} newDrug - The new drug to check
   * @param {string[]} currentMeds - Array of current medication names
   * @returns {Object[]} Array of DDI alerts
   */
  function checkNewDrug(newDrug, currentMeds) {
    if (!newDrug || !currentMeds || currentMeds.length === 0) {
      return [];
    }

    const allAlerts = [];

    for (const currentDrug of currentMeds) {
      const alerts = checkCuratedDDI(newDrug, currentDrug);
      allAlerts.push(...alerts);
    }

    return allAlerts
      .sort((a, b) => b.severityInfo.priority - a.severityInfo.priority);
  }

  /**
   * Format alerts as HTML for display
   */
  function formatAlertsHTML(alerts) {
    if (!alerts || alerts.length === 0) {
      return '<div class="ddi-no-alerts">Fant ingen varsler om interaksjoner</div>';
    }

    let html = '<div class="ddi-alerts">';

    alerts.forEach((alert, index) => {
      html += `
        <div class="ddi-alert ${alert.severityInfo.class}">
          <div class="ddi-alert-header">
            <span class="ddi-severity-badge">${alert.severityInfo.label}</span>
            <span class="ddi-summary">${escapeHtml(alert.summary)}</span>
          </div>
          <div class="ddi-alert-body">
            <p class="ddi-detail">${escapeHtml(alert.detail)}</p>
            <p class="ddi-recommendation"><strong>Anbefaling:</strong> ${escapeHtml(alert.recommendation)}</p>
          </div>
          <div class="ddi-alert-footer">
            <span class="ddi-source">Kilde: ${escapeHtml(alert.source)}</span>
          </div>
        </div>
      `;
    });

    html += '</div>';
    return html;
  }

  /**
   * Format alerts for CDS Hooks response
   */
  function formatForCDSHooks(alerts) {
    return alerts.map((alert, index) => ({
      uuid: `ddi-alert-${index}`,
      summary: alert.summary,
      indicator: alert.severity === 'Major' ? 'critical' : alert.severity === 'Moderate' ? 'warning' : 'info',
      detail: `${alert.detail}\n\nAnbefaling: ${alert.recommendation}`,
      source: {
        label: 'NOTxGNN DDI Checker',
        url: 'https://notxgnn.yao.care/'
      }
    }));
  }

  function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  // Export
  global.TwTxGNN = global.TwTxGNN || {};
  global.TwTxGNN.DDIChecker = {
    load: loadDDIIndex,
    checkInteractions: checkInteractions,
    checkNewDrug: checkNewDrug,
    formatAlertsHTML: formatAlertsHTML,
    formatForCDSHooks: formatForCDSHooks,
    SEVERITY: SEVERITY
  };

  // Auto-load when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadDDIIndex);
  } else {
    loadDDIIndex();
  }

})(typeof window !== 'undefined' ? window : this);
