import java.io.*;
import java.util.*;

public class MatchQueriesWithAOL {
	
	public static HashMap<String, Integer> isPresent;
	public static HashMap<String, Integer> taskNo;
	public static HashMap<String, Integer> dslr;
	public static HashMap<String, Integer> wedding;
	public static HashMap<String, Integer> games;
	public static HashMap<String, Integer> guitar;
	public static HashMap<String, Integer> download;
	public static HashMap<String, Integer> blog;
	public static HashMap<String, Integer> stream;

	public static void main(String[] args) throws Exception {
		isPresent = new HashMap<String, Integer>();
		taskNo = new HashMap<String, Integer>();
		dslr = new HashMap<String, Integer>();
		wedding = new HashMap<String, Integer>();
		games = new HashMap<String, Integer>();
		guitar = new HashMap<String, Integer>();
		download = new HashMap<String, Integer>();
		blog = new HashMap<String, Integer>();
		stream = new HashMap<String, Integer>();
		getExtraAOLQueries();
		System.exit(0);
		readQueries();
		readAOL();
		howManyCommon();
		
	}
	
	public static void getExtraAOLQueries() throws IOException
	{
		String filename = "/Users/rishabhmehrotra/dev/workspace/TaskBasedUserModeling/src/data/AOL/AOL1.txt";
		BufferedReader br;
		String line = "";
		int start = 1;
		String prevUserID = "";
		int c=0, count=10;
		while(count>0)
		{
			filename = "/Users/rishabhmehrotra/dev/workspace/TaskBasedUserModeling/src/data/AOL/AOL"+count+".txt";
			
			br = new BufferedReader(new FileReader(filename));
			line = br.readLine();line = br.readLine();
			while(line!=null)
			{
				try{
					c++;
					//if(c==100) break;
					String parts[] = line.split("\t");
					String userID = "";


					if(line.length()<1 || parts.length<1) {line = br.readLine();continue;}
					String qq = parts[1];
					if(qq.contains("buy") && (qq.contains("dslr") || qq.contains("camera") || qq.contains("nikon") || qq.contains("canon"))) if(dslr.containsKey(qq)) {int tt = dslr.get(qq);tt++;dslr.put(qq,tt);}else dslr.put(qq, 0);
					if(qq.contains("wedding")) if(wedding.containsKey(qq)) {int tt = wedding.get(qq);tt++;wedding.put(qq,tt);}else wedding.put(qq, 0);
					if(qq.contains("play") && qq.contains("game")) if(games.containsKey(qq)) {int tt = games.get(qq);tt++;games.put(qq,tt);}else games.put(qq, 0);
					if(qq.contains("guitar") && qq.contains("learn")) if(guitar.containsKey(qq)) {int tt = guitar.get(qq);tt++;guitar.put(qq,tt);}else guitar.put(qq, 0);
					if(qq.contains("download") && (qq.contains("video") || qq.contains("movie") || qq.contains("song"))) if(download.containsKey(qq)) {int tt = download.get(qq);tt++;download.put(qq,tt);}else download.put(qq, 0);
					if((qq.contains("write") || qq.contains("start") || qq.contains("site")) && qq.contains("blog")) if(blog.containsKey(qq)) {int tt = blog.get(qq);tt++;blog.put(qq,tt);}else blog.put(qq, 0);
					if(qq.contains("stream") && (qq.contains("live") || qq.contains("match") || qq.contains("game"))) if(stream.containsKey(qq)) {int tt = stream.get(qq);tt++;stream.put(qq,tt);}else stream.put(qq, 0);
				}
				catch(Exception e){e.printStackTrace();}
				line = br.readLine();
			}
			System.out.println("Done with "+count);
			count--;
		}
		FileWriter fstream0 = new FileWriter("/Users/rishabhmehrotra/dev/UCL/projects/subtasks/data/extra/wedding.AOL.txt");
		FileWriter fstream1 = new FileWriter("/Users/rishabhmehrotra/dev/UCL/projects/subtasks/data/extra/dslr.AOL.txt");
		FileWriter fstream2 = new FileWriter("/Users/rishabhmehrotra/dev/UCL/projects/subtasks/data/extra/games.AOL.txt");
		FileWriter fstream3 = new FileWriter("/Users/rishabhmehrotra/dev/UCL/projects/subtasks/data/extra/guitar.AOL.txt");
		FileWriter fstream4 = new FileWriter("/Users/rishabhmehrotra/dev/UCL/projects/subtasks/data/extra/blog.AOL.txt");
		FileWriter fstream5 = new FileWriter("/Users/rishabhmehrotra/dev/UCL/projects/subtasks/data/extra/stream.AOL.txt");
		FileWriter fstream6 = new FileWriter("/Users/rishabhmehrotra/dev/UCL/projects/subtasks/data/extra/download.AOL.txt");
		BufferedWriter out0 = new BufferedWriter(fstream0);
		BufferedWriter out1 = new BufferedWriter(fstream1);
		BufferedWriter out2 = new BufferedWriter(fstream2);
		BufferedWriter out3 = new BufferedWriter(fstream3);
		BufferedWriter out4 = new BufferedWriter(fstream4);
		BufferedWriter out5 = new BufferedWriter(fstream5);
		BufferedWriter out6 = new BufferedWriter(fstream6);
		Iterator<String> itr0 = wedding.keySet().iterator();
		Iterator<String> itr1 = dslr.keySet().iterator();
		Iterator<String> itr2 = games.keySet().iterator();
		Iterator<String> itr3 = guitar.keySet().iterator();
		Iterator<String> itr4 = blog.keySet().iterator();
		Iterator<String> itr5 = stream.keySet().iterator();
		Iterator<String> itr6 = download.keySet().iterator();
		while(itr0.hasNext()) {String qq = itr0.next();int tt = wedding.get(qq);if(tt>10) out0.write(qq+"\t"+0+"\t0"+"\n");}out0.close();
		while(itr1.hasNext()) {String qq = itr1.next();int tt = dslr.get(qq);if(tt>0) out1.write(qq+"\t"+0+"\t0"+"\n");}out1.close();
		while(itr2.hasNext()) {String qq = itr2.next();int tt = games.get(qq);if(tt>10) out2.write(qq+"\t"+0+"\t0"+"\n");}out2.close();
		while(itr3.hasNext()) {String qq = itr3.next();int tt = guitar.get(qq);if(tt>0) out3.write(qq+"\t"+0+"\t0"+"\n");}out3.close();
		while(itr4.hasNext()) {String qq = itr4.next();int tt = blog.get(qq);if(tt>0) out4.write(qq+"\t"+0+"\t0"+"\n");}out4.close();
		while(itr5.hasNext()) {String qq = itr5.next();int tt = stream.get(qq);if(tt>0) out5.write(qq+"\t"+0+"\t0"+"\n");}out5.close();
		while(itr6.hasNext()) {String qq = itr6.next();int tt = download.get(qq);if(tt>10) out6.write(qq+"\t"+0+"\t0"+"\n");}out6.close();
	}
	
	public static void howManyCommon() throws IOException
	{
		FileWriter fstream0 = new FileWriter("/Users/rishabhmehrotra/dev/UCL/projects/subtasks/data/0.allQueries.freq.nUsers.AOL.txt");
		FileWriter fstream1 = new FileWriter("/Users/rishabhmehrotra/dev/UCL/projects/subtasks/data/1.allQueries.freq.nUsers.AOL.txt");
		FileWriter fstream2 = new FileWriter("/Users/rishabhmehrotra/dev/UCL/projects/subtasks/data/2.allQueries.freq.nUsers.AOL.txt");
		FileWriter fstream3 = new FileWriter("/Users/rishabhmehrotra/dev/UCL/projects/subtasks/data/3.allQueries.freq.nUsers.AOL.txt");
		FileWriter fstream4 = new FileWriter("/Users/rishabhmehrotra/dev/UCL/projects/subtasks/data/4.allQueries.freq.nUsers.AOL.txt");
		FileWriter fstream5 = new FileWriter("/Users/rishabhmehrotra/dev/UCL/projects/subtasks/data/5.allQueries.freq.nUsers.AOL.txt");
		FileWriter fstream6 = new FileWriter("/Users/rishabhmehrotra/dev/UCL/projects/subtasks/data/6.allQueries.freq.nUsers.AOL.txt");
		BufferedWriter out0 = new BufferedWriter(fstream0);
		BufferedWriter out1 = new BufferedWriter(fstream1);
		BufferedWriter out2 = new BufferedWriter(fstream2);
		BufferedWriter out3 = new BufferedWriter(fstream3);
		BufferedWriter out4 = new BufferedWriter(fstream4);
		BufferedWriter out5 = new BufferedWriter(fstream5);
		BufferedWriter out6 = new BufferedWriter(fstream6);
		
		Iterator<String> itr = isPresent.keySet().iterator();
		int c1=0,c2=0;
		int t0=0,t1=0,t2=0,t3=0,t4=0,t5=0,t6=0;
		while(itr.hasNext())
		{
			c1++;
			String q = itr.next();
			int r = isPresent.get(q);
			if(r==1) c2++;
			int t  = taskNo.get(q);
			if(r==1)
			switch (t)
			{
			case 0: out0.write(q+"\t"+0+"\t"+0+"\n");t0++;break;
			case 1: out1.write(q+"\t"+0+"\t"+0+"\n");t1++;break;
			case 2: out2.write(q+"\t"+0+"\t"+0+"\n");t2++;break;
			case 3: out3.write(q+"\t"+0+"\t"+0+"\n");t3++;break;
			case 4: out4.write(q+"\t"+0+"\t"+0+"\n");t4++;break;
			case 5: out5.write(q+"\t"+0+"\t"+0+"\n");t5++;break;
			case 6: out6.write(q+"\t"+0+"\t"+0+"\n");t6++;break;
			}
		}
		System.out.println(c2+"  "+c1);
		System.out.println(t0+" "+t1+" "+t2+" "+t3+" "+t4+" "+t5+" "+t6);
		out0.close();out1.close();out2.close();out3.close();out4.close();out5.close();out6.close();
	}
	
	public static void readQueries() throws Exception
	{
		BufferedReader br;
		String line = "";
		int c=0, count=6;
		while(count>=0)
		{
			String filename = "/Users/rishabhmehrotra/dev/UCL/projects/subtasks/data/"+count+".allQueries.freq.nUsers.txt";
			
			br = new BufferedReader(new FileReader(filename));
			line = br.readLine();
			int tt=0;
			while(line!=null)
			{
				if(line.length()<5){line = br.readLine();continue;}
				
				 String parts[] = line.split("\t");
				 String qq = parts[0];
				 if(!isPresent.containsKey(qq))
					 {isPresent.put(qq, new Integer(0));tt++;}
				 if(!taskNo.containsKey(qq))
					 taskNo.put(qq, new Integer(count));
				 line = br.readLine();
			}
			br.close();
			count--;
			System.out.println("Done with "+count+"read: "+tt);
			System.out.println("Size of isPrssesent: "+isPresent.size());
		}
		System.out.println("Done reading ALL QUERIES\nNo of queries read: "+isPresent.size());
		//System.exit(0);
	}
	
	public static void readAOL() throws Exception
	{
		String filename = "/Users/rishabhmehrotra/dev/workspace/TaskBasedUserModeling/src/data/AOL/AOL1.txt";
		BufferedReader br;
		String line = "";
		int start = 1;
		String prevUserID = "";
		int c=0, count=10;
		while(count>0)
		{
			filename = "/Users/rishabhmehrotra/dev/workspace/TaskBasedUserModeling/src/data/AOL/AOL"+count+".txt";
			
			br = new BufferedReader(new FileReader(filename));
			line = br.readLine();line = br.readLine();
			while(line!=null)
			{
				try{
					c++;
					//if(c==100) break;
					String parts[] = line.split("\t");
					String userID = "";


					if(line.length()<1 || parts.length<1) {line = br.readLine();continue;}
					String qq = parts[1];
					if(isPresent.containsKey(qq))
					{
						isPresent.put(qq, new Integer(1));
					}
				}
				catch(Exception e){e.printStackTrace();}
				line = br.readLine();
			}
			System.out.println("Done with "+count);
			count--;
		}
	}
}
