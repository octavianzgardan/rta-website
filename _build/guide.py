# Guide: articoli con URL propri
import json, os
from layout import *

HERE = os.path.dirname(__file__)
OLD = json.load(open(os.path.join(HERE, "articoli_vecchi.json"), encoding="utf-8"))

def fix_old(k, c):
    if k == "1":
        c = c.replace("<p>Il legale rappresentante dell'impresa può anche fare da RT per la propria azienda, a condizione di avere almeno 3 anni consecutivi di esperienza nel ruolo — ma non può farlo per altre aziende.</p>",
            "<p>Il legale rappresentante può fare da RT solo per la propria impresa. Con la Delibera n. 6/2025, in vigore dal 2 gennaio 2026, la dispensa dalla verifica richiede tre anni di esperienza <strong>e</strong> un diploma di scuola superiore: molti titolari di piccole imprese non possono più autonominarsi. Ne parlo qui: <a href=\"/guide/delibera-6-2025-legale-rappresentante-rt/\">il titolare può ancora fare da RT?</a></p>")
        c = c.replace("il canone mensile parte da circa <strong>€200/mese</strong>. Puoi calcolare il preventivo preciso per la tua situazione direttamente da questo sito.",
            "il canone parte da <strong>€290/mese</strong>, prezzo finale. Trovi il <a href=\"/prezzi/\">listino completo</a> o puoi <a href=\"/preventivo/\">calcolare il preventivo</a> in un minuto.")
    if k == "7":
        c = c.replace("<li>Un <strong>Responsabile Tecnico</strong> con i requisiti previsti per la categoria</li>",
            "<li>Il ruolo di <strong>Responsabile Tecnico</strong>, che in Categoria 6 è assunto dal legale rappresentante dell'impresa</li>")
        c = c.replace("<p>Mi occupo dell'intero percorso: verifica preliminare dei requisiti, preparazione e presentazione della domanda di iscrizione in Categoria 6, nomina come Responsabile Tecnico e supporto sugli adempimenti documentali del Reg. CE 1013/2006 in base ai flussi e ai Paesi coinvolti. Rinnovi e variazioni sono inclusi, come per le altre categorie.</p>",
            "<p>Mi occupo della verifica preliminare dei requisiti, della preparazione e presentazione della domanda di iscrizione in Categoria 6 e del supporto sugli adempimenti documentali in base ai flussi e ai Paesi coinvolti. Tieni presente che le regole europee sulle spedizioni di rifiuti sono state riformate (Regolamento UE 2024/1157) e che dal 2027 è prevista la piattaforma elettronica europea per i documenti di spedizione: conviene organizzarsi per tempo.</p>")
        c = c.replace("compila il questionario sul sito selezionando la Categoria 6 e ricevi una proposta su misura entro 48 ore.",
            "<a href=\"/contatti/\">scrivimi</a> indicando Paesi, rifiuti e mezzi e ricevi una proposta su misura entro 48 ore lavorative.")
    c = c.replace("Il preventivo si calcola in tempo reale direttamente da questo sito.", "Puoi <a href=\"/preventivo/\">calcolare il preventivo</a> in un minuto.")
    return c

SLUGS = {
    "1": ("responsabile-tecnico-ambientale-cos-e", "2026-04-01"),
    "2": ("categoria-4-categoria-5-differenze", "2026-04-01"),
    "3": ("iscrizione-albo-gestori-ambientali-guida", "2026-04-01"),
    "4": ("rentri-fir-digitale-trasportatori", "2026-04-01"),
    "5": ("classi-albo-gestori-ambientali", "2026-04-01"),
    "6": ("nuovo-mezzo-variazione-albo", "2026-04-01"),
    "7": ("categoria-6-trasporto-transfrontaliero-guida", "2026-04-01"),
    "8": ("trasporto-raee-albo", "2026-04-01"),
}
DESCS = {
    "1": "Chi è il Responsabile Tecnico dell'Albo Gestori Ambientali, cosa fa, chi può esserlo dopo la Delibera 6/2025 e quanto costa un RT esterno.",
    "2": "Categoria 4 o Categoria 5 dell'Albo Gestori Ambientali: differenze tra rifiuti non pericolosi e pericolosi e come capire dove rientra la tua azienda.",
    "3": "Come iscriversi all'Albo Nazionale Gestori Ambientali passo passo: prerequisiti, documenti, pagamenti, tempi e durata dell'iscrizione.",
    "4": "RENTRI e FIR digitale per le aziende di trasporto rifiuti: obblighi dal 15 settembre 2026, chi è obbligato, costi e iscrizione.",
    "5": "Classi dimensionali dell'Albo Gestori Ambientali dalla F alla A: tonnellate, requisiti e come passare alla classe superiore.",
    "6": "Nuovo mezzo per il trasporto rifiuti: cosa comunicare all'Albo entro 30 giorni, documenti, idoneità tecnica e utilizzo immediato.",
    "7": "Categoria 6 dell'Albo per il trasporto transfrontaliero di rifiuti: chi deve iscriversi, regole europee sulle spedizioni e pratica.",
    "8": "Trasporto RAEE dopo l'abrogazione della Categoria 3-bis: quando basta il portale RAEE e quando servono Albo in Cat. 4/5 e RT.",
}

NEW = [
    {
        "slug": "responsabile-tecnico-dimesso-30-giorni",
        "tag": "Urgente",
        "title": "Il tuo Responsabile Tecnico se ne va: cosa fare entro 30 giorni per non perdere l'iscrizione",
        "desc": "Il Responsabile Tecnico ha lasciato l'incarico? Hai 30 giorni per nominarne uno nuovo all'Albo Gestori Ambientali. Cosa fare, documenti e rischi.",
        "date": "2026-10-26",
        "content": """
<p>Il tuo Responsabile Tecnico va in pensione, si dimette, cambia lavoro o non supera la verifica di aggiornamento. Succede più spesso di quanto si pensi, e quasi sempre nel momento sbagliato. La regola da ricordare è una sola: <strong>l'impresa non può restare senza RT</strong>, e hai un tempo limitato per sostituirlo.</p>
<h2>Il termine: 30 giorni</h2>
<p>Quando il Responsabile Tecnico cessa l'incarico, l'impresa deve nominarne uno nuovo e comunicarlo all'Albo entro 30 giorni. Se il termine passa senza un nuovo RT idoneo, la Sezione regionale avvia la cancellazione dell'iscrizione per le categorie interessate.</p>
<p>La cancellazione è molto peggio di una sanzione: per tornare a trasportare quei rifiuti serve una nuova iscrizione, con nuovi costi, nuovi tempi e mezzi fermi nel frattempo.</p>
<h2>Cosa fare, in ordine</h2>
<ol>
<li><strong>Annota la data di cessazione</strong> del vecchio RT: è da lì che partono i 30 giorni.</li>
<li><strong>Individua il nuovo RT</strong>: un dipendente con i requisiti, il titolare se ha i requisiti della <a href="/guide/delibera-6-2025-legale-rappresentante-rt/">Delibera 6/2025</a>, oppure un RT esterno.</li>
<li><strong>Prepara i documenti</strong>: documento d'identità del legale rappresentante, intercalare RT firmato, dichiarazione di compatibilità dell'incarico del nuovo RT con gli altri suoi incarichi.</li>
<li><strong>Presenta la variazione all'Albo</strong> tramite il portale telematico, con la PEC aziendale attiva.</li>
<li><strong>Controlla l'esito</strong>: la Sezione può chiedere integrazioni, e vanno date in fretta.</li>
</ol>
<h2>Gli errori più comuni</h2>
<ul>
<li>Accorgersi del problema alla terza settimana, quando il tempo per firme e integrazioni non basta più.</li>
<li>Dare per scontato che il titolare possa fare da RT: dopo la Delibera 6/2025 servono requisiti precisi.</li>
<li>Avere la PEC aziendale scaduta o piena: l'Albo comunica solo lì.</li>
<li>Dimenticare la dichiarazione di compatibilità del nuovo RT, che va allegata alla pratica.</li>
</ul>
<h2>Quanto costa sostituire l'RT</h2>
<p>Con me il canone da RT esterno parte da €290 al mese, senza vincoli, e la pratica di subentro ha priorità quando la scadenza è vicina. <a href="/subentro-responsabile-tecnico/">Ecco come funziona il subentro</a>.</p>
""",
    },
    {
        "slug": "delibera-6-2025-legale-rappresentante-rt",
        "tag": "Normativa 2026",
        "title": "Delibera 6/2025: il titolare può ancora fare da Responsabile Tecnico?",
        "desc": "Delibera Albo n. 6/2025 in vigore dal 2 gennaio 2026: quando il legale rappresentante può fare da Responsabile Tecnico, diploma, esperienza e verifiche.",
        "date": "2026-10-26",
        "content": """
<p>Fino a poco tempo fa, in molte piccole imprese di trasporto rifiuti il Responsabile Tecnico era semplicemente il titolare. Dal <strong>2 gennaio 2026</strong> le regole sono cambiate: la <strong>Delibera n. 6 del 26 novembre 2025</strong> del Comitato nazionale dell'Albo ha riscritto requisiti e verifiche dei Responsabili Tecnici, sostituendo diverse delibere precedenti.</p>
<h2>Cosa cambia per il legale rappresentante</h2>
<ul>
<li>Il legale rappresentante può essere dispensato dalla verifica di idoneità solo se ha <strong>almeno tre anni di esperienza</strong> e un <strong>diploma di scuola secondaria di secondo grado</strong>.</li>
<li>Anche quando è dispensato, può fare da RT <strong>esclusivamente per la propria impresa</strong>, non per altre.</li>
<li>Se cessa dalla carica di legale rappresentante, per continuare a fare l'RT deve sostenere la verifica di aggiornamento entro i termini previsti.</li>
</ul>
<h2>Chi resta scoperto</h2>
<p>Il caso più frequente è il titolare di una ditta individuale, magari un autospurgo o un piccolo trasportatore, con tanti anni di esperienza ma senza diploma superiore. Con le nuove regole non può più autonominarsi Responsabile Tecnico. Le alternative sono due: superare la verifica di idoneità presso l'Albo, oppure nominare un RT esterno.</p>
<h2>E se il Responsabile Tecnico non supera la verifica?</h2>
<p>Le sessioni di verifica del 2026 sono ripartite con quiz nuovi, e non tutti le superano al primo tentativo. In alcune situazioni il legale rappresentante può coprire il ruolo per un periodo limitato, ma è una soluzione temporanea. Se l'impresa resta senza RT valgono i <a href="/guide/responsabile-tecnico-dimesso-30-giorni/">30 giorni per la sostituzione</a>.</p>
<h2>Cosa ti conviene fare</h2>
<ol>
<li>Controlla chi è oggi l'RT della tua impresa e con quali requisiti è stato nominato.</li>
<li>Se è il titolare, verifica diploma ed esperienza rispetto alla nuova delibera.</li>
<li>Se qualcosa non torna, non aspettare un controllo o il rinnovo: regolarizza prima.</li>
</ol>
<div class="note">Questa guida riassume i punti principali per le piccole imprese di trasporto. Ogni caso ha i suoi dettagli: con il <a href="/contatti/">check-up gratuito</a> verifico la tua situazione specifica.</div>
""",
    },
    {
        "slug": "fir-digitale-problemi-trasportatori",
        "tag": "FIR digitale",
        "title": "FIR digitale dal 15 settembre 2026: i problemi più comuni dei trasportatori e come risolverli",
        "desc": "FIR digitale (xFIR) e RENTRI per trasportatori: iscrizione con attività sbagliata, deleghe, firma, app, registro non trasmesso. Problemi comuni e soluzioni.",
        "date": "2026-10-26",
        "content": """
<p>Dal <strong>15 settembre 2026</strong> il formulario cartaceo non è più valido per i soggetti iscritti al RENTRI: i rifiuti viaggiano con il FIR digitale (xFIR). Nelle prime settimane ho visto ripetersi sempre gli stessi intoppi. Eccoli, con la soluzione.</p>
<h2>1. Iscrizione RENTRI con l'attività sbagliata</h2>
<p>Chi fa solo trasporto deve risultare iscritto come trasportatore, senza attività che non svolge (per esempio il recupero). Un'attività sbagliata complica tutto il resto, dai formulari al registro. <strong>Soluzione:</strong> verifica i dati dell'iscrizione nella tua area RENTRI e correggili se serve.</p>
<h2>2. Chi compila non è abilitato</h2>
<p>Il titolare si è iscritto, ma l'impiegata o l'autista che compilano i formulari non sono tra le persone incaricate. <strong>Soluzione:</strong> aggiungi le persone che operano per l'impresa, oppure delega il consulente che gestisce i formulari per te.</p>
<h2>3. Manca il certificato per la firma</h2>
<p>Per firmare i FIR sul RENTRI serve il certificato di firma rilasciato dal sistema, nella sezione dei certificati digitali RENTRI. È diverso dai certificati per l'interoperabilità con i gestionali. <strong>Soluzione:</strong> richiedi il certificato giusto per chi deve firmare.</p>
<h2>4. L'app non è abbinata al telefono</h2>
<p>L'autista deve poter firmare al momento del carico e dello scarico. Il telefono va abbinato dalla sezione dedicata ai dispositivi mobili, con il codice QR di attivazione. <strong>Soluzione:</strong> fai l'abbinamento in ufficio, con calma, prima del primo viaggio, non sul piazzale del cliente.</p>
<h2>5. Registro salvato ma non trasmesso</h2>
<p>Nel registro di carico e scarico sul RENTRI salvare una registrazione non basta: va trasmessa con l'apposito comando. È l'errore più subdolo, perché a schermo sembra tutto a posto. <strong>Soluzione:</strong> controlla che ogni registrazione risulti trasmessa.</p>
<h2>6. Il produttore non è iscritto al RENTRI</h2>
<p>Privati, condomini e tante piccole imprese non sono iscritti. In questi casi spesso tocca al trasportatore emettere il formulario, con i dati del produttore. <strong>Soluzione:</strong> organizza un modello di raccolta dati da far compilare al cliente prima dell'intervento.</p>
<h2>7. "Il RENTRI non funziona, uso il cartaceo"</h2>
<p>Il FIR cartaceo è ammesso solo nei casi di malfunzionamento previsti dalle regole ministeriali, e va gestito secondo quelle istruzioni. Non è un'alternativa da usare quando è più comodo. <strong>Soluzione:</strong> tieni pronta la procedura di emergenza, ma usala solo quando serve davvero.</p>
<h2>Non vuoi pensarci tu?</h2>
<p>Posso configurare RENTRI, deleghe, firma e app per la tua impresa, oppure gestire io i tuoi FIR per conto tuo, a formulario o con un forfait mensile. <a href="/fir-digitale-xfir/">Dettagli su FIR digitale e RENTRI</a>.</p>
""",
    },
]

def article_page(slug, tag, title, desc, date, content):
    path = f"/guide/{slug}/"
    items = [("Home", "/"), ("Guide", "/guide/"), (title, path)]
    def it(d):
        y, m, g = d.split("-"); mesi = ["gennaio","febbraio","marzo","aprile","maggio","giugno","luglio","agosto","settembre","ottobre","novembre","dicembre"]
        return f"{int(g)} {mesi[int(m)-1]} {y}"
    meta = f"{tag} · Aggiornata il {UPDATED_IT}" if date != UPDATED else f"{tag} · {it(date)}"
    body = f'''<section class="page-hero"><div class="wrap">{crumbs([("Home","/"),("Guide","/guide/"),(tag,path)])}<h1>{title}</h1><div class="article-meta">{meta} · di Octavian Zgardan, Responsabile Tecnico Ambientale</div></div></section>
<section class="s"><div class="wrap article-layout">
  <article class="prose">{content}
    <div class="author-box"><img src="/assets/octavian-zgardan.jpg" alt="Octavian Zgardan" width="58" height="58" loading="lazy"><p><strong>Octavian Zgardan</strong> è Responsabile Tecnico iscritto all'Albo Nazionale Gestori Ambientali (Cat. 1, 4, 5). Segue imprese di trasporto rifiuti su Albo, RENTRI e FIR digitale. <a href="/chi-sono/">Chi sono</a>.</p></div>
  </article>
  <aside class="article-side">
    <div class="side-cta"><h3>Hai un dubbio sulla tua situazione?</h3><p>Scrivimi su WhatsApp: rispondo in giornata, la prima risposta è gratis.</p>{btn_wa("WhatsApp", "Ciao Octavian, ho letto la guida «" + title + "» e ho una domanda: ", "btn-block")}{btn_call(None, "btn-block")}</div>
    <a class="card" href="/prezzi/"><h3>Prezzi pubblici</h3><p>RT esterno da €290/mese, prezzo finale.</p><span class="more">Vedi il listino →</span></a>
  </aside>
</div></section>
{cta_band()}'''
    art = {"@context": "https://schema.org", "@type": "Article", "headline": title, "description": desc,
           "datePublished": date, "dateModified": UPDATED, "inLanguage": "it-IT",
           "author": {"@type": "Person", "name": "Octavian Zgardan", "url": SITE + "/chi-sono/"},
           "publisher": {"@type": "Person", "name": "Octavian Zgardan"}, "mainEntityOfPage": SITE + path,
           "image": SITE + "/assets/octavian-zgardan.jpg"}
    return path, page(path, f"{title} | Guida", desc, body, [breadcrumb_schema(items), art])

def all_guides():
    out = []
    for g in NEW:
        out.append(dict(g, path=f"/guide/{g['slug']}/"))
    for k, v in OLD.items():
        slug, date = SLUGS[k]
        title = v["title"]
        out.append({"slug": slug, "tag": v["tag"].replace("Novità — ", ""), "title": title, "desc": DESCS[k], "date": date,
                    "content": fix_old(k, v["content"]), "path": f"/guide/{slug}/"})
    return out

def guide_index(guides):
    items = [("Home", "/"), ("Guide", "/guide/")]
    cards = "".join(f'<a class="card" href="{g["path"]}"><span class="badge">{g["tag"]}</span><h3>{g["title"]}</h3><p>{g["desc"]}</p><span class="more">Leggi →</span></a>' for g in guides)
    b = page_hero(items, "Guide su Albo Gestori Ambientali, RENTRI e FIR digitale",
                  "Scritte per titolari di imprese di trasporto rifiuti: cosa fare, entro quando, in parole semplici. Aggiornate alle regole in vigore a ottobre 2026.", False) + f'''
<section class="s"><div class="wrap"><div class="grid g3 guide-list">{cards}</div></div></section>
{cta_band()}'''
    return page("/guide/", "Guide Albo Gestori Ambientali, RENTRI e FIR digitale | Responsabile Tecnico",
                "Guide pratiche per imprese di trasporto rifiuti: Responsabile Tecnico, Delibera 6/2025, iscrizione Albo, classi, variazioni, RENTRI e FIR digitale, RAEE, Categoria 6.",
                b, [breadcrumb_schema(items)])
