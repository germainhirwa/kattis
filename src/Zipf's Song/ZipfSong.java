import java.io.*;
import java.util.*;

public class ZipfSong {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        SongComparator songComp = new SongComparator();

        String[] line = sc.readLine().split(" ");
        int n = Integer.parseInt(line[0]);
        int k = Integer.parseInt(line[1]);
        
        List<Song> album = new ArrayList<Song>();
        for (int i = 1; i <= n; i++) {
            String[] line2 = sc.readLine().split(" ");
            long songFreq = Long.parseLong(line2[0]);
            String songName = line2[1];
            album.add(new Song(songName, songFreq*i));
        }

        album.sort(songComp);
        for (int i = 0; i < k; i++) {
            writer.println(album.get(i));
        }

        writer.flush();
    }
}

class Song {
    public Long freq;
    public String name;

    public Song(String name, long freq) {
        this.name = name;
        this.freq = new Long(freq);
    }

    public String toString() {
        return this.name;
    }
}

class SongComparator implements Comparator<Song> {
    public int compare(Song s1, Song s2) {
        return s2.freq.compareTo(s1.freq);
    }

    public boolean equals(Object obj) {
        return this == obj;
    }
}