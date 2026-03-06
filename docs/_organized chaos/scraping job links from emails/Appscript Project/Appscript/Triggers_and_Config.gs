// ========= CONFIGURATION =========
const CONFIG = {
  GMAIL_LABELS_TO_PROCESS: ['AutoLog', 'Jobs/Alerts/LinkedIn'],
  // GMAIL_LABELS_TO_PROCESS: ['AutoLog', ],
  PROCESSED_LABEL_NAME: 'Jobs/Alerts/_Processed',
  EMAIL_SHEET_NAME: 'Emails',
  LINKS_SHEET_NAME: 'Jobs'
};
// ===============================

/**
 * Main trigger function to get new emails from Gmail and log them to the sheet.
 */
function processNewEmails() {
  try {
    const emailSheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(CONFIG.EMAIL_SHEET_NAME);
    if (!emailSheet) { throw new Error("Emails sheet not found."); }

    // 1. Get all existing KeyIDs from the sheet to prevent duplicates.
    const existingIds = new Set();
    if (emailSheet.getLastRow() > 1) {
      const keyIdColumn = getColumnIndexes(emailSheet)['KeyID'];
      const keyIdFormulas = emailSheet.getRange(2, keyIdColumn + 1, emailSheet.getLastRow() - 1, 1).getFormulas();
      keyIdFormulas.forEach(row => {
        // Extract the descriptive ID text from the hyperlink formula
        const match = row[0].match(/, "([^"]+)"\)/);
        if (match) existingIds.add(match[1]);
      });
    }

    const processedLabel = getOrCreateLabel(CONFIG.PROCESSED_LABEL_NAME);
    
    for (const labelName of CONFIG.GMAIL_LABELS_TO_PROCESS) {
      getOrCreateLabel(labelName);
      const searchQuery = `label:"${labelName}" -label:"${CONFIG.PROCESSED_LABEL_NAME}" newer_than:2d`;
      const threads = GmailApp.search(searchQuery);
      
      if (threads.length > 0) {
        for (const thread of threads) {
          const message = thread.getMessages()[0];
          if (!message) continue;

          // 2. Create the new, deterministic KeyID from the email's unique Gmail ID.
          const typePrefix = generateIdPrefix(determineEmailType(message));
          const newKeyID = `${typePrefix}_${message.getId()}`;

          // 3. Check if this ID already exists. If not, process the email.
          if (!existingIds.has(newKeyID)) {
            const emailData = parseEmailData(message, thread, newKeyID);
            if (emailData) {
              emailSheet.appendRow(emailData);
              Logger.log(`Logged new email to sheet: ${newKeyID}`);
              thread.addLabel(processedLabel);
              existingIds.add(newKeyID); // Add to our set to prevent dupes in the same run
            }
          } else {
            Logger.log(`Skipping duplicate email: ${newKeyID}`);
            thread.addLabel(processedLabel); // Mark as processed to skip in future searches
          }
        }
      }
    }
  } catch (e) {
    Logger.log(`An error occurred in processNewEmails: ${e.toString()}`);
  }
}
// function processNewEmails() {
//   compactSheet(CONFIG.EMAIL_SHEET_NAME); 
//   try {
//     // 1. Proactively ensure the "Processed" label exists BEFORE searching.
//     const processedLabel = getOrCreateLabel(CONFIG.PROCESSED_LABEL_NAME);
    
//     for (const labelName of CONFIG.GMAIL_LABELS_TO_PROCESS) {
//       // 2. Proactively ensure the label we are searching FOR also exists.
//       getOrCreateLabel(labelName); 

//       // 3. Build the search query with quotes for safety.
//       const searchQuery = `label:"${labelName}" -label:"${CONFIG.PROCESSED_LABEL_NAME}" newer_than:2d`;
      
//       Logger.log(`Searching with query: ${searchQuery}`);
//       const threads = GmailApp.search(searchQuery);
      
//       if (threads.length > 0) {
//         Logger.log(`Found ${threads.length} unprocessed email(s) with label: ${labelName}`);
//         const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(CONFIG.EMAIL_SHEET_NAME);
        
//         for (const thread of threads) {
//           const message = thread.getMessages()[0];
//           if (!message) { Logger.log('Error: Skipping thread with invalid message.'); continue; }
          
//           const emailData = parseEmailData(message, thread);
          
//           if (emailData) {
//             sheet.appendRow(emailData);
//             thread.addLabel(processedLabel);
//           }
//         }
//       }
//     }
//   } catch (e) {
//     // 4. If any error occurs, log it in detail.
//     Logger.log(`An error occurred in processNewEmails: ${e.toString()}`);
//     Logger.log(`Error details: ${e.stack}`);
//   }
// }

/**
 * Main trigger function to process emails from the sheet and extract links.
 */
function processEmailLinks() {
  compactSheet(CONFIG.LINKS_SHEET_NAME);

  const emailSheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(CONFIG.EMAIL_SHEET_NAME);
  if (emailSheet.getLastRow() < 2) {
    Logger.log('No data rows found in "Emails" sheet to process.');
    return;
  }
  
  // Get both the display values and the underlying formulas from the sheet
  const dataRange = emailSheet.getRange(2, 1, emailSheet.getLastRow() - 1, emailSheet.getLastColumn());
  const data = dataRange.getValues();
  const formulas = dataRange.getFormulas(); // This gets all hyperlink formulas
  const colIdx = getColumnIndexes(emailSheet);

  for (let i = 0; i < data.length; i++) {
    const row = data[i];
    const qtyTranscribed = row[colIdx['QuantityTranscribed']];
    
    if (qtyTranscribed == 0 || qtyTranscribed === '' || qtyTranscribed === null) {
      const emailType = row[colIdx['EmailType']];
      let extractedLinks = []; 

      // Route to the correct parser
      if (emailType === 'lensa (default)') {
        extractedLinks = parseLensaEmail(row[colIdx['Contents']]);
      } else if (emailType.startsWith('LinkedIn Alert')) {
        extractedLinks = parseLinkedInEmail(row[colIdx['Contents']]);
      }

      if (extractedLinks.length > 0) {
        // Add a server-side timestamp to each extracted link
        extractedLinks.forEach(link => {
          link['Timestamp'] = new Date();
        });
        
        // Get the full HYPERLINK formula from the "KeyID" column for this row
        const emailKeyIDFormula = formulas[i][colIdx['KeyID']];
        
        // Pass the entire formula string to the logging function
        logLinksToSheet(extractedLinks, emailKeyIDFormula);
        
        const rowNumber = i + 2;
        emailSheet.getRange(rowNumber, colIdx['QuantityTranscribed'] + 1).setValue(extractedLinks.length);
        emailSheet.getRange(rowNumber, colIdx['TimeTranscribed'] + 1).setValue(new Date());
      }
    }
  }
}