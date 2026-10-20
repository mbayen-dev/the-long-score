/* ---- constellation layout + audio + influence data ---- */
const LAYOUT = { // peak = year of their best-known work; lane 0 stage, 1 orchestra, 2 keyboard and chamber room
  vivaldi:{peak:1725,lane:1,dy:0}, bach:{peak:1730,lane:2,dy:0}, handel:{peak:1741,lane:0,dy:0},
  haydn:{peak:1790,lane:1,dy:0}, mozart:{peak:1785,lane:0,dy:0}, beethoven:{peak:1805,lane:1,dy:0},
  schubert:{peak:1822,lane:2,dy:0}, berlioz:{peak:1830,lane:1,dy:0}, chopin:{peak:1835,lane:2,dy:-34},
  schumann:{peak:1841,lane:2,dy:34}, liszt:{peak:1849,lane:2,dy:-34}, verdi:{peak:1853,lane:0,dy:0},
  wagner:{peak:1865,lane:0,dy:0}, tchaikovsky:{peak:1878,lane:1,dy:0}, grieg:{peak:1875,lane:2,dy:34},
  brahms:{peak:1885,lane:1,dy:0}, dvorak:{peak:1893,lane:1,dy:0}, mahler:{peak:1902,lane:1,dy:0}
};
const LANES = ["The stage","The orchestra","The keyboard room"];
const CLIPS = {
  vivaldi:{piece:"Spring, first movement (The Four Seasons)",by:"John Harrison, violin"},
  bach:{piece:"Cello Suite no. 1, Prelude"},
  handel:{piece:"Water Music, Hornpipe",by:"U.S. Marine Band chamber orchestra"},
  haydn:{piece:"Symphony no. 94, slow movement",by:"Boston Symphony Orchestra, Koussevitzky"},
  mozart:{piece:"Piano Concerto no. 21, slow movement (excerpt)"},
  beethoven:{piece:"Symphony no. 5, first movement"},
  schubert:{piece:"Symphony no. 8 \"Unfinished\", first movement"},
  berlioz:{piece:"Symphonie fantastique, March to the Scaffold",by:"Orchestre Lamoureux, Markevitch, 1962"},
  chopin:{piece:"Nocturne in E flat, op. 9 no. 2"},
  schumann:{piece:"Carnaval",by:"Sergei Rachmaninoff, piano (historic recording)"},
  liszt:{piece:"Hungarian Rhapsody no. 2"},
  verdi:{piece:"La traviata, Libiamo ne' lieti calici"},
  wagner:{piece:"Die Walküre, Ride of the Valkyries"},
  brahms:{piece:"Symphony no. 4, first movement",by:"Musopen Symphony Orchestra"},
  tchaikovsky:{piece:"Swan Lake, Act 2 extract"},
  dvorak:{piece:"Symphony no. 9 \"From the New World\", Largo"},
  grieg:{piece:"Peer Gynt, In the Hall of the Mountain King",by:"Musopen Symphony Orchestra"},
  mahler:{piece:"Symphony no. 5, Adagietto",by:"Peabody Symphony Orchestra"}
};
const EDGES = [
 ["vivaldi","bach","Bach copied out and rearranged several Vivaldi concertos, learning Italian concerto form from them."],
 ["bach","mozart","In Vienna around 1782 Mozart discovered Bach's fugues, and his writing grew more intricate."],
 ["handel","haydn","Haydn heard Handel's oratorios in London in 1791 and wrote The Creation soon after."],
 ["haydn","mozart","Close friends. Mozart dedicated six string quartets to Haydn."],
 ["haydn","beethoven","Beethoven took lessons from Haydn in Vienna from 1792."],
 ["mozart","beethoven","Beethoven's early concertos are modeled on Mozart's."],
 ["beethoven","schubert","Schubert revered Beethoven and asked to be buried near him."],
 ["beethoven","berlioz","Hearing Beethoven's symphonies in Paris in the 1820s changed Berlioz's idea of the orchestra."],
 ["berlioz","liszt","Liszt heard the Symphonie fantastique and made a piano transcription of it."],
 ["chopin","liszt","Friends and rivals in Paris, trading ideas about the piano."],
 ["schumann","chopin","Schumann was one of Chopin's earliest champions in print."],
 ["schumann","brahms","Schumann introduced the 20-year-old Brahms to the world in his essay \"New Paths\"."],
 ["liszt","wagner","Liszt staged Wagner's Lohengrin in Weimar in 1850 and later became his father-in-law."],
 ["liszt","grieg","Liszt praised Grieg's piano concerto and encouraged him to keep going."],
 ["brahms","dvorak","Brahms recommended Dvořák to his own publisher."],
 ["wagner","mahler","Mahler conducted Wagner's operas and inherited his enormous orchestral ambition."],
 ["verdi","wagner","Born the same year, 1813, and rivals in opera. They never met."],
 ["tchaikovsky","dvorak","Tchaikovsky invited Dvořák to Russia in 1890, and the two became friends."]
];
