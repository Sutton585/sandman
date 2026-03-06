/**
 * A special function that runs when the spreadsheet is opened.
 * Adds a custom menu to the UI.
 */
function onOpen() {
  SpreadsheetApp.getUi()
      .createMenu('Automation Tools')
      .addItem('Clean Up Recent Test Data', 'cleanUpRecentTestData')
      .addToUi();
}

/**
 * [FINAL] Logs an array of extracted link objects to the "Jobs" sheet dynamically.
 * @param {Array<Object>} linksArray Array of link objects from a parser.
 * @param {string} emailKeyID The KeyID of the source email (can be a placeholder).
 */
function logLinksToSheet(linksArray, emailKeyID) {
  const linksSheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(CONFIG.LINKS_SHEET_NAME);
  if (!linksSheet) {
    Logger.log(`Error: Could not find a sheet named "${CONFIG.LINKS_SHEET_NAME}".`);
    return;
  }
  
  const colIdx = getColumnIndexes(linksSheet);
  const headers = Object.keys(colIdx);
  const rowsToAdd = [];

  for (const linkData of linksArray) {
    const newRow = new Array(headers.length);

    // If an EmailKeyID was passed, add it to the data object.
    if (emailKeyID) {
      linkData['EmailKeyID'] = emailKeyID;
    }
    
    // Dynamically place each piece of data in the correct column based on the header.
    headers.forEach(header => {
      newRow[colIdx[header]] = linkData[header] || null;
    });
    
    rowsToAdd.push(newRow);
  }
  
  if (rowsToAdd.length > 0) {
    linksSheet.getRange(linksSheet.getLastRow() + 1, 1, rowsToAdd.length, headers.length).setValues(rowsToAdd);
    Logger.log(`Logged ${rowsToAdd.length} new link(s) to the "${CONFIG.LINKS_SHEET_NAME}" sheet.`);
  }
}

/**
 * Finds and removes all blank rows from the middle of a specified sheet.
 * @param {string} sheetName The name of the sheet to clean up.
 */
function compactSheet(sheetName) {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(sheetName);
  if (!sheet || sheet.getLastRow() < 2) {
    return; // Do nothing if the sheet doesn't exist or is empty
  }

  const data = sheet.getDataRange().getValues();
  const rowsToDelete = [];

  // Find all the blank rows
  data.forEach((row, index) => {
    // A row is considered blank if all its cells joined together make an empty string
    if (row.join('') === '') {
      // We add 1 to the index to get the actual row number
      rowsToDelete.push(index + 1);
    }
  });

  // Delete the rows from the bottom up to avoid shifting row numbers
  if (rowsToDelete.length > 0) {
    for (let i = rowsToDelete.length - 1; i >= 0; i--) {
      sheet.deleteRow(rowsToDelete[i]);
    }
    Logger.log(`Compacted sheet "${sheetName}", removed ${rowsToDelete.length} blank row(s).`);
  }
}

/**
 * Logs an array of extracted link objects to the "Links" sheet dynamically.
 * @param {Array<Object>} linksArray Array of link objects from the parser.
 * @param {string} emailKeyID The KeyID of the source email.
 */

// function logLinksToSheet(linksArray, emailKeyID) {
//   // const linksSheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(LINKS_SHEET_NAME);
//   const linksSheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(CONFIG.LINKS_SHEET_NAME);
//   const colIdx = getColumnIndexes(linksSheet);
//   const headers = Object.keys(colIdx);
//   const rowsToAdd = [];

//   for (const link of linksArray) {
//     const newRow = new Array(headers.length);

//     // This object now contains all the new fields our parser extracts.
//     const linkData = {
//       'KeyID': generateKeyID(),
//       'EmailKeyID': emailKeyID,
//       'Timestamp': new Date(),
//       'Title': link.title,
//       'URL': link.url,
//       'Description': link.description,
//       'FullContent': link.fullContent,
//       'Employer': link.employer,
//       'Location': link.location,
//       'Comp': link.comp,
//       'PrioritizedList': link.prioritizedList

//     };
    
//     // This part dynamically places the data in the correct column.
//     headers.forEach(header => {
//       newRow[colIdx[header]] = linkData[header] || null;
//     });
    
//     rowsToAdd.push(newRow);
//   }
  
//   if (rowsToAdd.length > 0) {
//     linksSheet.getRange(linksSheet.getLastRow() + 1, 1, rowsToAdd.length, headers.length).setValues(rowsToAdd);
//   }
// }


/**
 * Reads the header row of a sheet and returns an object mapping column names to their index.
 */
function getColumnIndexes(sheet) {
  const headers = sheet.getRange(1, 1, 1, sheet.getLastColumn()).getValues()[0];
  const colMap = {};
  headers.forEach((header, i) => {
    if (header) { // Only add header if it's not empty
      colMap[header] = i;
    }
  });
  return colMap;
}

/**
 * Generates a unique ID based on the timestamp and a random number.
 */
function generateKeyID() {
  return new Date().getTime().toString(36) + Math.random().toString(36).slice(2);
}

/**
 * Ensures a Gmail label exists, creating it if necessary.
 */
function getOrCreateLabel(labelName) {
  let label = GmailApp.getUserLabelByName(labelName);
  if (!label) {
    label = GmailApp.createLabel(labelName);
  }
  return label;
}

/**
 * Finds all data logged across 'Emails' and 'Jobs' sheets in the last minute
 * and deletes them after user confirmation.
 */
function cleanUpRecentTestData() {
  const ui = SpreadsheetApp.getUi();
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const emailSheet = ss.getSheetByName(CONFIG.EMAIL_SHEET_NAME);
  const jobsSheet = ss.getSheetByName(CONFIG.LINKS_SHEET_NAME);

  if (!emailSheet || !jobsSheet) {
    ui.alert('Error: Could not find the "Emails" or "Jobs" sheet.');
    return;
  }

  // Helper function to get all timestamps from a sheet
  const getTimestamps = (sheet, colName) => {
    if (sheet.getLastRow() < 2) return [];
    const colIdx = getColumnIndexes(sheet);
    if (colIdx[colName] === undefined) return [];
    const values = sheet.getRange(2, colIdx[colName] + 1, sheet.getLastRow() - 1, 1).getValues();
    return values.flat().filter(Boolean).map(date => new Date(date));
  };

  // 1. Get all timestamps and find the absolute most recent one
  const emailTimestamps = getTimestamps(emailSheet, 'TimeLogged');
  const jobTimestamps = getTimestamps(jobsSheet, 'Timestamp');
  const allTimestamps = [...emailTimestamps, ...jobTimestamps];

  if (allTimestamps.length === 0) {
    ui.alert('No data found to clean up.');
    return;
  }

  const mostRecentTime = new Date(Math.max.apply(null, allTimestamps));
  const oneMinuteAgo = mostRecentTime.getTime() - 60000;

  // 2. Identify all recent rows to delete from both sheets
  const getRowsToDelete = (sheet, colName) => {
    if (sheet.getLastRow() < 2) return [];
    const colIdx = getColumnIndexes(sheet);
    if (colIdx[colName] === undefined) return [];
    const timestamps = sheet.getRange(2, colIdx[colName] + 1, sheet.getLastRow() - 1, 1).getValues();
    const rowsToDelete = [];
    timestamps.forEach((ts, i) => {
      if (new Date(ts[0]).getTime() >= oneMinuteAgo) {
        rowsToDelete.push(i + 2); // +2 for 0-index and header
      }
    });
    return rowsToDelete;
  };

  const emailRowsToDelete = getRowsToDelete(emailSheet, 'TimeLogged');
  const jobRowsToDelete = getRowsToDelete(jobsSheet, 'Timestamp');
  const totalRows = emailRowsToDelete.length + jobRowsToDelete.length;

  if (totalRows === 0) {
    ui.alert('No recent test data found (logged within the last minute).');
    return;
  }

  // 3. Confirm with the user
  const response = ui.alert('Confirm Deletion', `Found ${emailRowsToDelete.length} email(s) and ${jobRowsToDelete.length} job(s) from the last test run. Are you sure you want to delete all ${totalRows} rows?`, ui.ButtonSet.YES_NO);

  if (response == ui.Button.YES) {
    // 4. Delete rows from the bottom up to avoid shifting indices
    for (let i = jobRowsToDelete.length - 1; i >= 0; i--) {
      jobsSheet.deleteRow(jobRowsToDelete[i]);
    }
    for (let i = emailRowsToDelete.length - 1; i >= 0; i--) {
      emailSheet.deleteRow(emailRowsToDelete[i]);
    }
    ui.alert(`Successfully deleted ${totalRows} rows.`);
  }
}

// function doPost(e) {
//   try {
//     const shortcutData = JSON.parse(e.postData.contents);

//     // 1. Get the fully parsed data, including the definitive KeyID.
//     const finalData = parseJobData(shortcutData.content, shortcutData.url);

//     // --- NEW: LOGIC TO FIND AND LINK TO THE ORIGINAL EMAIL RECORD ---
//     const linksSheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(CONFIG.LINKS_SHEET_NAME);
//     const colIdx = getColumnIndexes(linksSheet);
//     let originalEmailKeyID = 'n/a'; // Default value

//     if (linksSheet.getLastRow() > 1) {
//       const allData = linksSheet.getRange(2, 1, linksSheet.getLastRow() - 1, linksSheet.getLastColumn()).getValues();
//       const allFormulas = linksSheet.getRange(2, 1, linksSheet.getLastRow() - 1, linksSheet.getLastColumn()).getFormulas();

//       // Find a row that has the same KeyID as the one we just parsed.
//       const originalRecordIndex = allData.findIndex(row => row[colIdx['KeyID']] === finalData.KeyID);

//       // If we found a match, grab its EmailKeyID formula.
//       if (originalRecordIndex !== -1) {
//         originalEmailKeyID = allFormulas[originalRecordIndex][colIdx['EmailKeyID']];
//       }
//     }
//     // --- END NEW LOGIC ---

//     // 3. Add the timestamp and the (potentially found) EmailKeyID.
//     finalData['Timestamp'] = new Date();
//     finalData['EmailKeyID'] = originalEmailKeyID;

//     // 4. Log the complete data object to the sheet.
//     logLinksToSheet([finalData]);

//     return ContentService.createTextOutput(JSON.stringify({ 'status': 'success' }))
//       .setMimeType(ContentService.MimeType.JSON);
//   } catch (error) {
//     return ContentService.createTextOutput(JSON.stringify({ 'status': 'error', 'message': error.toString(), 'stack': error.stack }))
//       .setMimeType(ContentService.MimeType.JSON);
//   }
// }
/**
 * [FINAL] Handles pre-processed data, links it to an original email record if one exists, and logs it.
 */
function doPost(e) {
  try {
    const linksSheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(CONFIG.LINKS_SHEET_NAME);
    if (!linksSheet) { throw new Error("Sheet not found: " + CONFIG.LINKS_SHEET_NAME); }

    const params = JSON.parse(e.postData.contents);
    let emailKeyIDToLog = 'FROM_SHORTCUT'; // Default value

    // --- NEW: LOGIC TO FIND AND LINK TO THE ORIGINAL EMAIL RECORD ---
    if (linksSheet.getLastRow() > 1) {
      const colIdx = getColumnIndexes(linksSheet);
      const allData = linksSheet.getRange(2, 1, linksSheet.getLastRow() - 1, linksSheet.getLastColumn()).getValues();
      const allFormulas = linksSheet.getRange(2, 1, linksSheet.getLastRow() - 1, linksSheet.getLastColumn()).getFormulas();

      // Find a row that has the same KeyID as the one from the Shortcut.
      const originalRecordIndex = allData.findIndex(row => row[colIdx['KeyID']] === params.KeyID);

      // If we found a match, grab its EmailKeyID formula.
      if (originalRecordIndex !== -1) {
        const foundFormula = allFormulas[originalRecordIndex][colIdx['EmailKeyID']];
        // Make sure it's a hyperlink and not just 'FROM_SHORTCUT'
        if (foundFormula.startsWith('=HYPERLINK')) {
          emailKeyIDToLog = foundFormula;
        }
      }
    }
    // --- END NEW LOGIC ---

    // Add the final server-side data
    params['Timestamp'] = new Date();
    params['EmailKeyID'] = emailKeyIDToLog;

    const headers = Object.keys(getColumnIndexes(linksSheet));
    const newRow = new Array(headers.length);
    headers.forEach(header => {
      newRow[getColumnIndexes(linksSheet)[header]] = params[header] || null;
    });

    linksSheet.appendRow(newRow);

    return ContentService.createTextOutput(JSON.stringify({ 'status': 'success' }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({ 'status': 'error', 'message': error.toString(), 'stack': error.stack }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
/**
 * [STABLE] Handles incoming, pre-processed data from the Shortcut and logs it.
 */
// function doPost(e) {
//   try {
//     const linksSheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(CONFIG.LINKS_SHEET_NAME);
//     if (!linksSheet) { throw new Error("Sheet not found: " + CONFIG.LINKS_SHEET_NAME); }

//     const colIdx = getColumnIndexes(linksSheet);
//     const headers = Object.keys(colIdx);

//     // This function expects the data to be fully parsed and cleaned by the Shortcut.
//     const params = JSON.parse(e.postData.contents);

//     // Add the server-side timestamp and a placeholder EmailKeyID
//     params['Timestamp'] = new Date();
//     params['EmailKeyID'] = 'FROM_SHORTCUT';

//     const newRow = new Array(headers.length);
//     headers.forEach(header => {
//       newRow[colIdx[header]] = params[header] || null;
//     });

//     linksSheet.appendRow(newRow);

//     return ContentService.createTextOutput(JSON.stringify({ 'status': 'success' }))
//       .setMimeType(ContentService.MimeType.JSON);

//   } catch (error) {
//     return ContentService.createTextOutput(JSON.stringify({ 'status': 'error', 'message': error.toString(), 'stack': error.stack }))
//       .setMimeType(ContentService.MimeType.JSON);
//   }
// }
/**
 * [STABLE] Handles incoming, pre-processed data from the Shortcut and logs it.
 */
// function doPost(e) {
//   try {
//     compactSheet(CONFIG.LINKS_SHEET_NAME);
//     const linksSheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(CONFIG.LINKS_SHEET_NAME);
//     if (!linksSheet) { throw new Error("Sheet not found: " + CONFIG.LINKS_SHEET_NAME); }

//     const colIdx = getColumnIndexes(linksSheet);
//     const headers = Object.keys(colIdx);

//     // This function expects the data to be fully parsed and cleaned by the Shortcut.
//     const params = JSON.parse(e.postData.contents);

//     // Add the server-side timestamp.
//     params['Timestamp'] = new Date();

//     const newRow = new Array(headers.length);
//     headers.forEach(header => {
//       newRow[colIdx[header]] = params[header] || null;
//     });

//     linksSheet.appendRow(newRow);

//     return ContentService.createTextOutput(JSON.stringify({ 'status': 'success' }))
//       .setMimeType(ContentService.MimeType.JSON);

//   } catch (error) {
//     return ContentService.createTextOutput(JSON.stringify({ 'status': 'error', 'message': error.toString(), 'stack': error.stack }))
//       .setMimeType(ContentService.MimeType.JSON);
//   }
// }

/**
 * A helper to determine the source from a URL.
 */
function getSourceFromUrl(url) {
  if (!url) return 'unknown';
  if (url.includes('linkedin.com')) return 'linkedin';
  if (url.includes('indeed.com')) return 'indeed';
  return 'unknown';
}

/**
 * [IMPROVED] Sanitizes a URL and generates a consistent KeyID by determining the source internally.
 * @param {string} rawUrl The original, long URL.
 * @returns {Object} An object containing the cleaned 'url' and 'keyID'.
 */
function sanitizeUrlAndGetKey(rawUrl) {
  const source = getSourceFromUrl(rawUrl); // Determines the source from the URL
  let cleanedUrl = rawUrl.split('?')[0];
  let keyID = `${source}_unknownID`;

  if (source === 'linkedin') {
    const match = rawUrl.match(/view\/(\d+)|JobId=([^&]+)|currentJobId=(\d+)/);
    if (match) {
      const id_from_url = match[1] || match[2] || match[3];
      keyID = `${source}_${id_from_url}`;
      cleanedUrl = `https://www.linkedin.com/jobs/view/${id_from_url}`;
    }
  } else if (source === 'indeed') {
    const tempUrl = rawUrl.split('&')[0];
    const delimiter = '=';
    const parts = tempUrl.split(delimiter);
    const id_from_url = parts[parts.length - 1];
    keyID = `${source}_${id_from_url}`;
    cleanedUrl = tempUrl;
  }

  return { url: cleanedUrl, keyID: keyID };
}