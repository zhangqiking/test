--�öγ���Ĺ���Ϊ��ԭʼ���ݹ淶������������ϴ

declare @j int
set @j=1
declare @file_num int
declare @temp char(10)            --tempΪ�±�����
declare @temp3 char(10)           --tempΪ�ɱ�����
select @file_num=max(FileID) from files
while @j<=@file_num
   begin
       select @temp=sheet_name from newfiles where  newfileID=@j
       select @temp3=sheet_name from files where  FileID=@j
       exec('create table ' +@temp+ '(ID int identity(1,1) not null, ���� char(10),�۸� float,������ float)')   --ʹ�ñ�������̬������
       exec('select * into ##tem from ' +@temp3)                                                                --��һ����ʱ�����ݸ��Ƶ��µ����ݱ���
       exec('insert into ' +@temp+'(����,�۸�,������) select ����,�۸�,������ from ##tem')
       drop table ##tem                                                                                         --ɾ��ȫ����ʱ��
       set @j=@j+1
       exec('delete from ' + @temp+ ' where ������ is null')
   end
        
   
        

--�öγ���Ĺ����Ǽ���ÿ֧��Ʊ��������


declare @i int
declare @n int
declare @temp1 float                                    --�����i֧��Ʊ�۸�
declare @temp2 float                                    --�����i+1֧��Ʊ�۸�
declare @sheet_name char(10)
declare @para_1 nvarchar(100)
declare @para_2 nvarchar(100)

declare @para_4 nvarchar(500)
declare @sql_4 nvarchar(500)

declare @sql_1 nvarchar(100)
declare @sql_2 nvarchar(100)

declare @result float

declare @maxID int
declare @ID int
set @ID=1
select @maxID=MAX(newfileID) from newfiles
print @maxID
while @ID<=@maxID
   begin
       select @sheet_name=sheet_name from newfiles where  newfileID=@ID
       exec('alter table ' +@sheet_name+ ' add shouyi decimal(18,4) not NULL default(0)')
       declare @sql nvarchar(1000)
       set @sql = 'select @n=max(ID) ' + ' from ' +@sheet_name
       exec sp_executesql @sql,N'@n int output',@n output
       print @n
       set @i=1
       while @i<=@n
       begin
        
         set @sql_1 = N'select @temp_out_1=�۸� ' + ' from ' +@sheet_name+ 'where ID=@tem'
         set @sql_2 = N'select @temp_out_2=�۸� ' + ' from ' +@sheet_name+ 'where ID=@tem+1'
         set @para_1 = N'@tem NVARCHAR(20),@temp_out_1 float output'
         set @para_2 = N'@tem NVARCHAR(20),@temp_out_2 float output'
         
         exec sp_executesql @sql_1,
                   @para_1,
                   @tem=@i,
                   @temp_out_1=@temp1 output;
                  
                   
          exec sp_executesql @sql_2,
                             @para_2,
                             @tem=@i,
                             @temp_out_2=@temp2 output;
                   
         
         set @result=(@temp2-@temp1)/@temp1
         print @result
         set @sql_4 =N'update ' +@sheet_name+ 'set shouyi=@r where ID=@tem+1'
         set @para_4 = N'@tem NVARCHAR(20),@r float'
         exec sp_executesql @sql_4,
                            @para_4,
                            @tem=@i,
                            @r=@result;
         set @i=@i+1
     end
     set @ID=@ID+1
end












/*
--��̬�����и�������ֵ�ķ���
declare @n nvarchar(10)
declare @sql nvarchar(1000)
declare @temp nvarchar(10)
select @temp=sheet_name from newfiles where  newfileID=1
set @sql = 'select @n=max(ID) ' + ' from ' +@temp
exec sp_executesql @sql,N'@n int output',@n output
print @n
*/


                      
