/**
 * Determines the EmailType based on the sender's email address.
 */
function determineEmailType(message) {
  const fromAddress = message.getFrom();
  const lowerCaseAddress = fromAddress.toLowerCase();
  
  if (lowerCaseAddress.includes('linkedin.com')) {
    const body = message.getPlainBody();
    const lines = body.split('\n');
    
    const alertLine = lines.find(line => line.includes('Your job alert for'));
    
    if (alertLine) {
      const alertTitle = alertLine.replace('Your job alert for', '').trim();
      return `LinkedIn Alert: ${alertTitle}`;
    }
    
    return 'LinkedIn (default)'; // Fallback for other LinkedIn emails
  } 
  
  if (lowerCaseAddress.includes('indeed.com')) return 'indeed (default)';
  if (lowerCaseAddress.includes('lensa.com')) return 'lensa (default)';
  if (lowerCaseAddress.includes('usebraintrust.com')) return 'braintrust (default)';
  
  // Fallback for all other unknown sources
  const emailRegex = /<(.+)>/;
  const match = fromAddress.match(emailRegex);
  const sourceEmail = match ? match[1] : fromAddress;
  return `${sourceEmail} (default)`;
}

/**
 * Creates a short, descriptive prefix from a long EmailType string.
 * @param {string} emailType The full EmailType (e.g., "LinkedIn Alert: "UX" OR "Usability"...")
 * @returns {string} A short prefix (e.g., "LNKD_UX_Usability_ProductDesign")
 */
function generateIdPrefix(emailType) {
  // Get the main part of the title after "Alert:"
  let titlePart = emailType.split('Alert:')[1] || emailType;
  
  // Remove quotes, parentheses, and location info
  titlePart = titlePart.replace(/"/g, '').replace(/\(.*?\)/g, '');
  titlePart = titlePart.split(' in ')[0].trim();
  
  // Split by "OR", take the first few parts, and join them.
  const keywords = titlePart.split(' OR ');
  const prefix = keywords.slice(0, 3).join('_').replace(/\s+/g, ''); // Take up to 3 keywords
  
  // Create a final, clean prefix
  let finalPrefix = `LNKD_${prefix}`;
  if (finalPrefix.length > 25) {
    finalPrefix = finalPrefix.substring(0, 25); // Truncate if it's too long
  }
  
  return finalPrefix;
}

/**
 * Parses the email message to extract data for the "Emails" sheet.
 * @param {GoogleAppsScript.Gmail.GmailMessage} message The Gmail message.
 * @param {GoogleAppsScript.Gmail.GmailThread} thread The full Gmail thread.
 * @param {string} descriptiveKeyID The pre-built, unique KeyID for the email.
 * @returns {Array|null} An array of data formatted for the "Emails" sheet row.
 */
function parseEmailData(message, thread, descriptiveKeyID) {
  const fromAddress = message.getFrom();
  const emailType = determineEmailType(message);
  let body = message.getPlainBody();
  let linkCount = 0;

  // Build the Google Sheets formula string using the passed-in KeyID
  const permalink = thread.getPermalink();
  const keyIdFormula = `=HYPERLINK("${permalink}", "${descriptiveKeyID}")`;

  // --- CONSOLIDATED LINK COUNTING LOGIC ---
  if (emailType.startsWith('LinkedIn Alert')) {
    const endMarker = 'See all jobs';
    const lastIndex = body.lastIndexOf(endMarker);
    if (lastIndex !== -1) {
      body = body.substring(0, lastIndex);
    }
    const separator = /-{10,}/;
    const jobChunks = body.split(separator);
    linkCount = jobChunks.length > 1 ? jobChunks.length -1 : (jobChunks.length > 0 ? 1 : 0);
  } else if (emailType === 'lensa (default)') {
    const separator = /\n\|\s*\|\s*!\[LE\]/;
    const cardChunks = body.split(separator);
    linkCount = cardChunks.length > 1 ? cardChunks.length - 1 : 0;
  }

  return [
    keyIdFormula, // Use the new formula
    message.getDate(),
    new Date(),
    fromAddress,
    emailType,
    body,
    linkCount,
    '0',
    null
  ];
}
/**
 * Parses the email message to extract data for the "Emails" sheet.
 * @param {GoogleAppsScript.Gmail.GmailMessage} message The Gmail message.
 * @param {GoogleAppsScript.Gmail.GmailThread} thread The full Gmail thread.
 * @returns {Array|null} An array of data formatted for the "Emails" sheet row.
 */
// function parseEmailData(message, thread) {
//   const fromAddress = message.getFrom();
//   const emailType = determineEmailType(message);
//   let body = message.getPlainBody();
//   let linkCount = 0;

//   // --- Create the Descriptive, Clickable KeyID ---
//   const keyID = generateKeyID(); // The original unique ID
//   const permalink = thread.getPermalink(); // Get the URL to the email

//   // Use our new helper to generate a smart, descriptive prefix.
//   const typePrefix = generateIdPrefix(emailType);
//   const descriptiveKeyID = `${typePrefix}_${keyID}`;

//   // Build the Google Sheets formula string
//   const keyIdFormula = `=HYPERLINK("${permalink}", "${descriptiveKeyID}")`;
//   // --- END ---

//   // --- CONSOLIDATED LINK COUNTING LOGIC ---
//   if (emailType.startsWith('LinkedIn Alert')) {
//     const endMarker = 'See all jobs';
//     const lastIndex = body.lastIndexOf(endMarker);
//     if (lastIndex !== -1) {
//       body = body.substring(0, lastIndex);
//     }
//     const separator = '---------------------------------------------------------';
//     linkCount = (body.match(new RegExp(separator, 'g')) || []).length;

//   } else if (emailType === 'lensa (default)') {
//     // This is the new part for counting Lensa links
//     const separator = /\n\|\s*\|\s*!\[LE\]/;
//     const cardChunks = body.split(separator);
//     linkCount = cardChunks.length > 1 ? cardChunks.length - 1 : 0;
//   }
//   // --- END CONSOLIDATED LOGIC ---
//   return [
//     keyIdFormula, // Use the new formula instead of the plain KeyID
//     message.getDate(),
//     new Date(),
//     fromAddress,
//     emailType,
//     body,
//     linkCount,
//     '0',
//     null
//   ];
// }

/**
 * Parses the email message to extract data for the "Emails" sheet.
 */
// function parseEmailData(message) {
//   const fromAddress = message.getFrom();
//   const emailType = determineEmailType(message);
//   const keyID = generateKeyID();
//   let body = message.getPlainBody();
//   let linkCount = 0;

//   // --- CONSOLIDATED LINK COUNTING LOGIC ---
//   if (emailType.startsWith('LinkedIn Alert')) {
//     const endMarker = 'See all jobs';
//     const lastIndex = body.lastIndexOf(endMarker);
//     if (lastIndex !== -1) {
//       body = body.substring(0, lastIndex);
//     }
//     const separator = '---------------------------------------------------------';
//     linkCount = (body.match(new RegExp(separator, 'g')) || []).length;

//   } else if (emailType === 'lensa (default)') {
//     // This is the new part for counting Lensa links
//     const separator = /\n\|\s*\|\s*!\[LE\]/;
//     const cardChunks = body.split(separator);
//     linkCount = cardChunks.length > 1 ? cardChunks.length - 1 : 0;
//   }
//   // --- END CONSOLIDATED LOGIC ---

//   return [
//     keyID,
//     message.getDate(),
//     new Date(),
//     fromAddress,
//     emailType,
//     body,
//     linkCount,
//     '0',
//     null
//   ];
// }