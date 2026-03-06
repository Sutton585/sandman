
/**
 * Cleans known junk headers from the start of a LinkedIn job card.
 * @param {string} cardText The raw text of a job card.
 * @returns {string} The cleaned text.
 */
function cleanJunkHeaders(cardText) {
  const junkPhrases = ['New jobs from your other alerts', 'match your preferences.'];
  let cleanedText = cardText;

  for (const phrase of junkPhrases) {
    if (cleanedText.includes(phrase)) {
      const junkHeaderIndex = cleanedText.indexOf(phrase);
      const tempCard = cleanedText.substring(junkHeaderIndex + phrase.length); // Start searching after the phrase
      const firstCharIndex = tempCard.search(/[a-zA-Z0-9]/);
      if (firstCharIndex !== -1) {
        cleanedText = tempCard.substring(firstCharIndex);
      }
    }
  }
  return cleanedText;
}

/**
 * Parses a LinkedIn email to extract individual job links and their details.
 * @param {string} contents The plain text body of the email.
 * @returns {Array<Object>} An array of objects, each containing the job details.
 */
function parseLinkedInEmail(contents) {
  const links = [];
  const foundUrls = {};

  // 1. Split the email content into job cards using the horizontal line.
  const separator = /^-{3,}$/m;;
  const cardChunks = contents.split(separator);

  // 2. Loop through each card to extract details.
  for (let card of cardChunks) {
    if (card.trim() === '') continue; // Skip empty chunks
    
    card = cleanJunkHeaders(card);

    const lines = card.split('\n').filter(line => line.trim() !== '');
    if (lines.length < 3) continue;

    let title = lines[0].trim();
    let employer = lines[1].trim();
    let location = lines[2].trim();
    let description = lines.slice(3).join(' ').trim();
    let url = '';

    //const urlMatch = card.match(/View job: (https?:\/\/[^\s]+)/);
    // if (urlMatch) {
    //   const rawUrl = urlMatch[1];
    //   const trackingIdIndex = rawUrl.indexOf('?trackingId=');
    //   url = (trackingIdIndex !== -1) ? rawUrl.substring(0, trackingIdIndex) : rawUrl;
    // }

    const urlMatch = card.match(/View job: (https?:\/\/[^\s]+)/);
    if (urlMatch) {
      const rawUrl = urlMatch[1];
      
      // Call our new helper to get the clean URL and KeyID
      const sanitizedData = sanitizeUrlAndGetKey(rawUrl);

      if (sanitizedData.url && !foundUrls[sanitizedData.url]) {
        links.push({
          'KeyID': sanitizedData.keyID, // Use the new KeyID
          'URL': sanitizedData.url,     // Use the new clean URL
          'Title': lines[0].trim(),
          'Employer': lines[1].trim(),
          'Location': lines[2].trim(),
          'Description': lines.slice(3).join(' ').trim(),
          'Comp': '',
          'FullContent': card.trim()
        });
        foundUrls[sanitizedData.url] = true;
      }
    }
  }
  Logger.log(`Extracted details for ${links.length} unique job links from LinkedIn email.`);
  return links;
}

