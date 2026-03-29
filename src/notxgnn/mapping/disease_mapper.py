"""疾病映射模組 - 葡萄牙語適應症/治療類別映射至 TxGNN 疾病本體"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd


# 葡萄牙語-英語疾病/症狀對照表
DISEASE_DICT = {
    # === Hjerte og kar (Cardiovascular) ===
    "høyt blodtrykk": "hypertension",
    "hypertensjon": "hypertension",
    "lavt blodtrykk": "hypotension",
    "hjerteinfarkt": "myocardial infarction",
    "angina pectoris": "angina",
    "hjerterytmeforstyrrelse": "arrhythmia",
    "atrieflimmer": "atrial fibrillation",
    "hjertesvikt": "heart failure",
    "koronarsykdom": "coronary artery disease",
    "dyp venetrombose": "deep vein thrombosis",
    "lungeemboli": "pulmonary embolism",
    "hyperkolesterolemi": "hypercholesterolemia",
    "dyslipidemi": "dyslipidemia",
    "aterosklerose": "atherosclerosis",
    "endokarditt": "endocarditis",
    "myokarditt": "myocarditis",
    "perikarditt": "pericarditis",
    # === Luftveier (Respiratory) ===
    "kronisk obstruktiv lungesykdom": "chronic obstructive pulmonary disease",
    "kols": "chronic obstructive pulmonary disease",
    "astma": "asthma",
    "lungebetennelse": "pneumonia",
    "bronkitt": "bronchitis",
    "influensa": "influenza",
    "tuberkulose": "tuberculosis",
    "cystisk fibrose": "cystic fibrosis",
    "søvnapné": "obstructive sleep apnea",
    "pustebesvær": "dyspnea",
    "emfysem": "emphysema",
    "bihulebetennelse": "sinusitis",
    "allergisk rhinitt": "allergic rhinitis",
    # === Fordøyelsessystemet (Gastrointestinal) ===
    "gastroøsofageal reflukssykdom": "gastroesophageal reflux disease",
    "halsbrann": "gastroesophageal reflux disease",
    "magesår": "gastric ulcer",
    "tolvfingertarmsår": "duodenal ulcer",
    "gastritt": "gastritis",
    "irritabel tarm-syndrom": "irritable bowel syndrome",
    "inflammatorisk tarmsykdom": "inflammatory bowel disease",
    "crohns sykdom": "crohn disease",
    "ulcerøs kolitt": "ulcerative colitis",
    "forstoppelse": "constipation",
    "diaré": "diarrhea",
    "kvalme": "nausea",
    "oppkast": "vomiting",
    "fettlever": "hepatic steatosis",
    "levercirrhose": "liver cirrhosis",
    "hepatitt": "hepatitis",
    "hepatitt b": "hepatitis b",
    "hepatitt c": "hepatitis c",
    "pankreatitt": "pancreatitis",
    "gallestein": "cholelithiasis",
    # === Nervesystemet (Neurological) ===
    "alzheimers sykdom": "alzheimer disease",
    "parkinsons sykdom": "parkinson disease",
    "epilepsi": "epilepsy",
    "multippel sklerose": "multiple sclerosis",
    "ms": "multiple sclerosis",
    "migrene": "migraine",
    "hodepine": "headache",
    "hjerneslag": "stroke",
    "nevropati": "neuropathy",
    "perifer nevropati": "peripheral neuropathy",
    "hjernehinnebetennelse": "meningitis",
    "hjernebetennelse": "encephalitis",
    # === Psykisk helse (Psychiatric) ===
    "depresjon": "depression",
    "alvorlig depresjon": "major depressive disorder",
    "angst": "anxiety disorder",
    "generalisert angstlidelse": "generalized anxiety disorder",
    "bipolar lidelse": "bipolar disorder",
    "schizofreni": "schizophrenia",
    "tvangslidelse": "obsessive-compulsive disorder",
    "posttraumatisk stresslidelse": "post-traumatic stress disorder",
    "ptsd": "post-traumatic stress disorder",
    "søvnløshet": "insomnia",
    "adhd": "attention deficit hyperactivity disorder",
    # === Endokrint system (Endocrine) ===
    "diabetes": "diabetes mellitus",
    "sukkersyke": "diabetes mellitus",
    "diabetes type 1": "type 1 diabetes mellitus",
    "diabetes type 2": "type 2 diabetes mellitus",
    "lavt stoffskifte": "hypothyroidism",
    "høyt stoffskifte": "hyperthyroidism",
    "struma": "goiter",
    "cushings syndrom": "cushing syndrome",
    "addisons sykdom": "addison disease",
    "fedme": "obesity",
    "overvekt": "obesity",
    "metabolsk syndrom": "metabolic syndrome",
    "urinsyregikt": "gout",
    # === Muskel og skjelett (Musculoskeletal) ===
    "leddgikt": "arthritis",
    "revmatoid artritt": "rheumatoid arthritis",
    "artrose": "osteoarthritis",
    "benskjørhet": "osteoporosis",
    "osteoporose": "osteoporosis",
    "systemisk lupus": "systemic lupus erythematosus",
    "fibromyalgi": "fibromyalgia",
    "bekhterevs sykdom": "ankylosing spondylitis",
    "senebetennelse": "tendinitis",
    "korsryggsmerter": "low back pain",
    # === Hudsykdommer (Dermatological) ===
    "psoriasis": "psoriasis",
    "eksem": "eczema",
    "atopisk eksem": "atopic dermatitis",
    "elveblest": "urticaria",
    "akne": "acne",
    "rosacea": "rosacea",
    "vitiligo": "vitiligo",
    "hårtap": "alopecia",
    "helvetesild": "herpes zoster",
    "forkjølelsessår": "herpes simplex",
    "soppinfeksjon": "fungal infection",
    # === Urinveier (Urological) ===
    "urinveisinfeksjon": "urinary tract infection",
    "blærebetennelse": "cystitis",
    "nyrebetennelse": "nephritis",
    "nyresvikt": "renal failure",
    "kronisk nyresykdom": "chronic kidney disease",
    "nyrestein": "nephrolithiasis",
    "godartet prostataforstørrelse": "benign prostatic hyperplasia",
    "urininkontinens": "urinary incontinence",
    # === Øyesykdommer (Ophthalmological) ===
    "grønn stær": "glaucoma",
    "glaukom": "glaucoma",
    "grå stær": "cataract",
    "katarakt": "cataract",
    "makuladegenerasjon": "macular degeneration",
    "konjunktivitt": "conjunctivitis",
    "diabetisk retinopati": "diabetic retinopathy",
    "tørre øyne": "dry eye syndrome",
    # === ØNH (ENT) ===
    "mellomørebetennelse": "otitis media",
    "halsbetennelse": "pharyngitis",
    "mandelbetennelse": "tonsillitis",
    "strupehodebetennelse": "laryngitis",
    "svimmelhet": "vertigo",
    # === Infeksjonssykdommer (Infectious) ===
    "hiv-infeksjon": "hiv infection",
    "aids": "acquired immunodeficiency syndrome",
    "malaria": "malaria",
    "covid-19": "covid-19",
    "koronavirus": "covid-19",
    "blodforgiftning": "sepsis",
    "sepsis": "sepsis",
    "candidose": "candidiasis",
    "toksoplasmose": "toxoplasmosis",
    # === Allergier (Allergic) ===
    "allergi": "allergy",
    "anafylaksi": "anaphylaxis",
    "allergisk astma": "allergic asthma",
    "høysnue": "allergic rhinitis",
    "kontakteksem": "contact dermatitis",
    "matallergi": "food allergy",
    # === Gynekologi (Gynecological) ===
    "endometriose": "endometriosis",
    "polycystisk ovariesyndrom": "polycystic ovary syndrome",
    "overgangsalder": "menopause",
    "menstruasjonssmerter": "dysmenorrhea",
    "livmorsvulst": "uterine fibroid",
    "svangerskapsforgiftning": "preeclampsia",
    # === Kreft (Oncological) ===
    "kreft": "cancer",
    "brystkreft": "breast cancer",
    "lungekreft": "lung cancer",
    "tarmkreft": "colorectal cancer",
    "prostatakreft": "prostate cancer",
    "leverkreft": "liver cancer",
    "magekreft": "stomach cancer",
    "bukspyttkjertelkreft": "pancreatic cancer",
    "leukemi": "leukemia",
    "lymfom": "lymphoma",
    "melanom": "melanoma",
    "nyrekreft": "kidney cancer",
    "blærekreft": "bladder cancer",
    "skjoldbruskkjertelkreft": "thyroid cancer",
    # === Generelle symptomer (General) ===
    "feber": "fever",
    "smerte": "pain",
    "kronisk smerte": "chronic pain",
    "betennelse": "inflammation",
    "hevelse": "edema",
    "tretthet": "fatigue",
    "blodmangel": "anemia",
    "anemi": "anemia",
}


def load_disease_vocab(filepath: Optional[Path] = None) -> pd.DataFrame:
    """載入 TxGNN 疾病詞彙表"""
    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "external" / "disease_vocab.csv"
    return pd.read_csv(filepath)


def build_disease_index(disease_df: pd.DataFrame) -> Dict[str, Tuple[str, str]]:
    """建立疾病名稱索引（關鍵詞 -> (disease_id, disease_name)）"""
    index = {}

    for _, row in disease_df.iterrows():
        disease_id = row["disease_id"]
        disease_name = row["disease_name"]
        name_upper = row["disease_name_upper"]

        # 完整名稱
        index[name_upper] = (disease_id, disease_name)

        # 提取關鍵詞（按空格和逗號分割）
        keywords = re.split(r"[,\s\-]+", name_upper)
        for kw in keywords:
            kw = kw.strip()
            if len(kw) > 3 and kw not in index:  # 只保留較長的關鍵詞
                index[kw] = (disease_id, disease_name)

    return index


def extract_indications(indication_str: str) -> List[str]:
    """從適應症/治療類別文字提取個別適應症

    使用葡萄牙語常見分隔符分割
    """
    if not indication_str:
        return []

    # 正規化
    text = indication_str.strip().lower()

    # 使用分隔符分割
    parts = re.split(r"[.;]", text)

    indications = []
    for part in parts:
        # 再用逗號細分
        sub_parts = re.split(r"[,/]", part)
        for sub in sub_parts:
            sub = sub.strip()
            # 移除常見前綴
            sub = re.sub(r"^(para |tratamento de |indicado para |usado para )", "", sub)
            # 移除常見後綴
            sub = re.sub(r"( e outros| etc\.?)$", "", sub)
            sub = sub.strip()
            if sub and len(sub) >= 2:
                indications.append(sub)

    return indications


def translate_indication(indication: str) -> List[str]:
    """將葡萄牙語適應症翻譯為英文關鍵詞"""
    keywords = []
    indication_lower = indication.lower()

    for pt, en in DISEASE_DICT.items():
        if pt in indication_lower:
            keywords.append(en.upper())

    return keywords


def map_indication_to_disease(
    indication: str,
    disease_index: Dict[str, Tuple[str, str]],
) -> List[Tuple[str, str, float]]:
    """將單一適應症映射到 TxGNN 疾病

    Returns:
        [(disease_id, disease_name, confidence), ...]
    """
    results = []

    # 翻譯為英文關鍵詞
    keywords = translate_indication(indication)

    for kw in keywords:
        # 完全匹配
        if kw in disease_index:
            disease_id, disease_name = disease_index[kw]
            results.append((disease_id, disease_name, 1.0))
            continue

        # 部分匹配
        for index_kw, (disease_id, disease_name) in disease_index.items():
            if kw in index_kw or index_kw in kw:
                results.append((disease_id, disease_name, 0.8))

    # 去重並按信心度排序
    seen = set()
    unique_results = []
    for disease_id, disease_name, conf in sorted(results, key=lambda x: -x[2]):
        if disease_id not in seen:
            seen.add(disease_id)
            unique_results.append((disease_id, disease_name, conf))

    return unique_results[:5]  # 最多返回 5 個匹配


def map_fda_indications_to_diseases(
    fda_df: pd.DataFrame,
    disease_df: Optional[pd.DataFrame] = None,
    indication_field: str = "CLASSE_TERAPEUTICA",
) -> pd.DataFrame:
    """將巴西 ANVISA 藥品治療類別映射到 TxGNN 疾病"""
    if disease_df is None:
        disease_df = load_disease_vocab()

    disease_index = build_disease_index(disease_df)

    results = []

    for _, row in fda_df.iterrows():
        # ANVISA 使用 CLASSE_TERAPEUTICA 而非適應症
        indication_str = row.get(indication_field, "")
        if not indication_str:
            continue

        # 提取個別適應症
        indications = extract_indications(indication_str)

        for ind in indications:
            # 翻譯並映射
            matches = map_indication_to_disease(ind, disease_index)

            if matches:
                for disease_id, disease_name, confidence in matches:
                    results.append({
                        "NUMERO_REGISTRO_PRODUTO": row.get("NUMERO_REGISTRO_PRODUTO", ""),
                        "NOME_PRODUTO": row.get("NOME_PRODUTO", ""),
                        "CLASSE_TERAPEUTICA": indication_str[:100],
                        "extracted_indication": ind,
                        "disease_id": disease_id,
                        "disease_name": disease_name,
                        "confidence": confidence,
                    })
            else:
                results.append({
                    "NUMERO_REGISTRO_PRODUTO": row.get("NUMERO_REGISTRO_PRODUTO", ""),
                    "NOME_PRODUTO": row.get("NOME_PRODUTO", ""),
                    "CLASSE_TERAPEUTICA": indication_str[:100],
                    "extracted_indication": ind,
                    "disease_id": None,
                    "disease_name": None,
                    "confidence": 0,
                })

    return pd.DataFrame(results)


def get_indication_mapping_stats(mapping_df: pd.DataFrame) -> dict:
    """計算適應症映射統計"""
    total = len(mapping_df)
    mapped = mapping_df["disease_id"].notna().sum()
    unique_indications = mapping_df["extracted_indication"].nunique()
    unique_diseases = mapping_df[mapping_df["disease_id"].notna()]["disease_id"].nunique()

    return {
        "total_indications": total,
        "mapped_indications": int(mapped),
        "mapping_rate": mapped / total if total > 0 else 0,
        "unique_indications": unique_indications,
        "unique_diseases": unique_diseases,
    }
